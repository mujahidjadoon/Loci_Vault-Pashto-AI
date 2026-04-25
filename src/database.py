import faiss
import numpy as np


class PashtoVectorStore:
    """
    Logic for the Digital Memory Palace.
    Stores Pashto text segments as spatial vectors.
    """

    def __init__(self, dimension=384):
        # Initialize FAISS index for L2 distance (Spatial similarity)
        self.index = faiss.IndexFlatL2(dimension)
        self.metadata = []

    def add_document_chunk(self, text, vector):
        """Places a document chunk into a specific 'Loci' (coordinate)"""
        vector_array = np.array([vector]).astype('float32')
        self.index.add(vector_array)
        self.metadata.append(text)

    def search_vault(self, query_vector, k=2):
        """Retrieves information from the closest spatial location"""
        vector_array = np.array([query_vector]).astype('float32')
        distances, indices = self.index.search(vector_array, k)

        # Return retrieved text from the vault
        return [self.metadata[i] for i in indices[0] if i != -1]