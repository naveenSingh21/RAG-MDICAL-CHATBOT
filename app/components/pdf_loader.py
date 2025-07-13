import os
from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from app.common.logger import get_logger
from app.common.custom_exception import CustomException
from app.config.config import DATA_PATH,CHUNK_SIZE,CHUNK_OVERLAP

logger = get_logger(__name__)

def load_pdf_files():
    try:
        # if not os.path.exists(file_path):
        #     raise CustomException(f"Data path {file_path} does not exist")
        # logger.info(f"Loading PDF files from {file_path}")
        loader = DirectoryLoader(DATA_PATH,glob="*.pdf",loader_cls=PyPDFLoader)
        documents = loader.load()
        if not documents:
            logger.warning("No PDF files found in the data path")
        else:
            logger.info(f"successfully loaded {len(documents)} documents")
        return documents
        
        
    except Exception as e:
        raise CustomException(e)
        return []

def create_textchunks(documents):
    try:
        if not documents:
            raise CustomException("No documents to create text chunks")
        logger.info(f"Creating text chunks for {len(documents)} documents")
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE,chunk_overlap=CHUNK_OVERLAP)
        text_chunks = text_splitter.split_documents(documents)

        logger.info(f"Generated {len(text_chunks)} text chunks")

        return text_chunks
    except Exception as e:
        error_message = CustomException("Failed to load",e)
        logger.error(str(error_message))
        return []