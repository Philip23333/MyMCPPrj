from abc import ABC, abstractclassmethod, abstractmethod
from typing import Optional

from langchain_community.chat_models import ChatOpenAI
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.embeddings import Embeddings
from utils.config_loader import load_config_by_name

model_conf = load_config_by_name('agemt')

class ModelFactory(ABC):
    @abstractmethod
    def create_model(self)->Optional[Embeddings|ChatOpenAI]:
        pass

class ChatModelFactory(ModelFactory):
    def create_model(self) -> ChatOpenAI:
        return ChatOpenAI(
            model=model_conf['DASH_SCOPE_MODEL_NAME'],
            api_key=model_conf["DASH_SCOPE_API_KEY"],
            base_url=model_conf["DASH_SCOPE_URL"],
        )

class EmbeddingModelFactory(ModelFactory):
    def create_model(self) -> Embeddings:
        # 这里需要根据实际情况返回一个Embeddings实例
        return DashScopeEmbeddings(
            model=model_conf['DASH_SCOPE_EMBEDDING_MODEL_NAME'],
            dashscope_api_key=model_conf['DASH_SCOPE_API_KEY'],
        )  # 替换为实际的Embeddings实现

def get_chat_model() -> ChatOpenAI:
    """创建并返回一个全新的ChatOpenAI实例（每次调用都生成新对象）"""
    return ChatModelFactory().create_model()

def get_embedding_model() -> Embeddings:
    """创建并返回一个全新的Embeddings实例（每次调用都生成新对象）"""
    return EmbeddingModelFactory().create_model()

chat_model = get_chat_model()
embedding_model = get_embedding_model()