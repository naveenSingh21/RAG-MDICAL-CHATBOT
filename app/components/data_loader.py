import os
from app.components.pdf_loader import load_pdf_files,create_textchunks
from app.components.vectorstore import save_vector_store
from app.config.config import DB_FAISS_PATH

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

def process_and_store_pdfs():
    try:
        logger.info("Making the vectorstore..")
        documnets = load_pdf_files()
        text_chunks = create_textchunks(documnets)
        save_vector_store(text_chunks)
        logger.info("Vector store craeted successfully...")
    except Exception as e:
        error_message = CustomException('Failed to create vector store')
        logger.error(str(error_message))

if __name__=="__main__":
    process_and_store_pdfs()
