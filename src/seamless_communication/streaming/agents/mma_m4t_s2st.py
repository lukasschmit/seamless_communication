# Copyright (c) Meta Platforms, Inc. and affiliates
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from seamless_communication.streaming.agents.offline_w2v_bert_encoder import (
    OfflineWav2VecBertEncoderAgent,
)
from seamless_communication.streaming.agents.online_feature_extractor import (
    OnlineFeatureExtractorAgent,
)
from seamless_communication.streaming.agents.online_text_decoder import (
    UnitYMMATextDecoderAgent,
)
from seamless_communication.streaming.agents.online_unit_decoder import (
    NARUnitYUnitDecoderAgent,
)
from seamless_communication.streaming.agents.silero_vad import SileroVADAgent
from seamless_communication.streaming.agents.online_vocoder import VocoderAgent
from seamless_communication.streaming.agents.pretssel_vocoder import PretsselVocoderAgent

from seamless_communication.streaming.agents.detokenizer import UnitYDetokenizerAgent
from seamless_communication.streaming.agents.unity_pipeline import (
    UnitYAgentPipeline,
    UnitYAgentTreePipeline,
)
from simuleval.utils import entrypoint


class MonotonicM4TS2STAgent(UnitYAgentPipeline):
    pipeline = [
        OnlineFeatureExtractorAgent,
        OfflineWav2VecBertEncoderAgent,
        UnitYMMATextDecoderAgent,
        NARUnitYUnitDecoderAgent,
        VocoderAgent,
    ]


class SeamlessS2STAgent(UnitYAgentPipeline):
    pipeline = [
        OnlineFeatureExtractorAgent,
        OfflineWav2VecBertEncoderAgent,
        UnitYMMATextDecoderAgent,
        NARUnitYUnitDecoderAgent,
        PretsselVocoderAgent,
    ]


class MonotonicM4TS2STVADAgent(UnitYAgentPipeline):
    pipeline = [
        SileroVADAgent,
        OnlineFeatureExtractorAgent,
        OfflineWav2VecBertEncoderAgent,
        UnitYMMATextDecoderAgent,
        NARUnitYUnitDecoderAgent,
        VocoderAgent,
    ]


class MonotonicM4TS2STJointVADAgent(UnitYAgentTreePipeline):
    pipeline = {
        SileroVADAgent: [OnlineFeatureExtractorAgent],
        OnlineFeatureExtractorAgent: [OfflineWav2VecBertEncoderAgent],
        OfflineWav2VecBertEncoderAgent: [UnitYMMATextDecoderAgent],
        UnitYMMATextDecoderAgent: [UnitYDetokenizerAgent, NARUnitYUnitDecoderAgent],
        UnitYDetokenizerAgent: [],
        NARUnitYUnitDecoderAgent: [VocoderAgent],
        VocoderAgent: [],
    }


class SeamlessS2STJointVADAgent(UnitYAgentTreePipeline):
    pipeline = {
        SileroVADAgent: [OnlineFeatureExtractorAgent],
        OnlineFeatureExtractorAgent: [OfflineWav2VecBertEncoderAgent],
        OfflineWav2VecBertEncoderAgent: [UnitYMMATextDecoderAgent],
        UnitYMMATextDecoderAgent: [UnitYDetokenizerAgent, NARUnitYUnitDecoderAgent],
        UnitYDetokenizerAgent: [],
        NARUnitYUnitDecoderAgent: [PretsselVocoderAgent],
        PretsselVocoderAgent: [],
    }
