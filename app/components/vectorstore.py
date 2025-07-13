from langchain_community.vectorstores import FAISS
from app.components.embeddings import get_embedding_model
import os

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

from app.config.config import DB_FAISS_PATH

logger = get_logger(__name__)

def load_vector_store():
    try:
        embedding_model = get_embedding_model()
        if os.path.exists(DB_FAISS_PATH):
            logger.info("loading existing vector store")
            return FAISS.load_local(DB_FAISS_PATH, embedding_model, allow_dangerous_deserialization=True)
        else:
            logger.warning("No vector store found..")
    except Exception as e:
        error_message = CustomException("Failed to load vector store")
        logger.error(str(error_message))


#creating new vector store
def save_vector_store(text_chunks):
    try:
        if not text_chunks:
            raise CustomException("No tetx chunks were found")
        logger.info("Genearting your new vectorstore")

        embedding_model = get_embedding_model()
        db = FAISS.from_documents(text_chunks,embedding_model)

        logger.info("Saving vector store")

        db.save_local(DB_FAISS_PATH)

        logger.info("Vectorstore saved successfully")

        return db
    except Exception as e:
        error_message = CustomException("Failed to create vector store")
        logger.error(str(error_message))

