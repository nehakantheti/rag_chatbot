from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime

class ModelName(str, Enum):
    GEMINI_1_0_PRO_VISION_LATEST = "gemini-1.0-pro-vision-latest"
    GEMINI_PRO_VISION = "gemini-pro-vision"
    GEMINI_1_5_PRO_LATEST = "gemini-1.5-pro-latest"
    GEMINI_1_5_PRO_001 = "gemini-1.5-pro-001"
    GEMINI_1_5_PRO_002 = "gemini-1.5-pro-002"
    GEMINI_1_5_PRO = "gemini-1.5-pro"
    GEMINI_1_5_FLASH_LATEST = "gemini-1.5-flash-latest"
    GEMINI_1_5_FLASH_001 = "gemini-1.5-flash-001"
    GEMINI_1_5_FLASH_001_TUNING = "gemini-1.5-flash-001-tuning"
    GEMINI_1_5_FLASH = "gemini-1.5-flash"
    GEMINI_1_5_FLASH_002 = "gemini-1.5-flash-002"
    GEMINI_1_5_FLASH_8B = "gemini-1.5-flash-8b"
    GEMINI_1_5_FLASH_8B_001 = "gemini-1.5-flash-8b-001"
    GEMINI_1_5_FLASH_8B_LATEST = "gemini-1.5-flash-8b-latest"
    GEMINI_1_5_FLASH_8B_EXP_0827 = "gemini-1.5-flash-8b-exp-0827"
    GEMINI_1_5_FLASH_8B_EXP_0924 = "gemini-1.5-flash-8b-exp-0924"
    GEMINI_2_5_PRO_EXP_03_25 = "gemini-2.5-pro-exp-03-25"
    GEMINI_2_5_PRO_PREVIEW_03_25 = "gemini-2.5-pro-preview-03-25"
    GEMINI_2_5_FLASH_PREVIEW_04_17 = "gemini-2.5-flash-preview-04-17"
    GEMINI_2_5_FLASH_PREVIEW_05_20 = "gemini-2.5-flash-preview-05-20"
    GEMINI_2_5_FLASH_PREVIEW_04_17_THINKING = "gemini-2.5-flash-preview-04-17-thinking"
    GEMINI_2_5_PRO_PREVIEW_05_06 = "gemini-2.5-pro-preview-05-06"
    GEMINI_2_0_FLASH_EXP = "gemini-2.0-flash-exp"
    GEMINI_2_0_FLASH = "gemini-2.0-flash"
    GEMINI_2_0_FLASH_001 = "gemini-2.0-flash-001"
    GEMINI_2_0_FLASH_EXP_IMAGE_GENERATION = "gemini-2.0-flash-exp-image-generation"
    GEMINI_2_0_FLASH_LITE_001 = "gemini-2.0-flash-lite-001"
    GEMINI_2_0_FLASH_LITE = "gemini-2.0-flash-lite"
    GEMINI_2_0_FLASH_PREVIEW_IMAGE_GENERATION = "gemini-2.0-flash-preview-image-generation"
    GEMINI_2_0_FLASH_LITE_PREVIEW_02_05 = "gemini-2.0-flash-lite-preview-02-05"
    GEMINI_2_0_FLASH_LITE_PREVIEW = "gemini-2.0-flash-lite-preview"
    GEMINI_2_0_PRO_EXP = "gemini-2.0-pro-exp"
    GEMINI_2_0_PRO_EXP_02_05 = "gemini-2.0-pro-exp-02-05"
    GEMINI_EXP_1206 = "gemini-exp-1206"
    GEMINI_2_0_FLASH_THINKING_EXP_01_21 = "gemini-2.0-flash-thinking-exp-01-21"
    GEMINI_2_0_FLASH_THINKING_EXP = "gemini-2.0-flash-thinking-exp"
    GEMINI_2_0_FLASH_THINKING_EXP_1219 = "gemini-2.0-flash-thinking-exp-1219"
    GEMINI_2_5_FLASH_PREVIEW_TTS = "gemini-2.5-flash-preview-tts"
    GEMINI_2_5_PRO_PREVIEW_TTS = "gemini-2.5-pro-preview-tts"
    LEARNLM_2_0_FLASH_EXPERIMENTAL = "learnlm-2.0-flash-experimental"
    GEMMA_3_1B_IT = "gemma-3-1b-it"
    GEMMA_3_4B_IT = "gemma-3-4b-it"
    GEMMA_3_12B_IT = "gemma-3-12b-it"
    GEMMA_3_27B_IT = "gemma-3-27b-it"
    GEMMA_3N_E4B_IT = "gemma-3n-e4b-it"


class QueryInput(BaseModel):
    question: str
    session_id: str = Field(default=None)
    model: ModelName = Field(default=ModelName.GEMINI_2_0_FLASH)

class QueryResponse(BaseModel):
    answer: str
    session_id: str
    model: ModelName

class DocumentInfo(BaseModel):
    id: int
    filename: str
    upload_timestamp: datetime

class DeleteFileRequest(BaseModel):
    file_id: int