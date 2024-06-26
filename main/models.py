# models.py

import json
import os
from django.db import models
from django.utils.translation import gettext_lazy as _
import nltk
import wikipedia
import numpy as np
from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Téléchargement des corpus nécessaires pour nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('punkt')

# Modèle Article
class Article(models.Model):
    title = models.CharField(_('title'), max_length=200)
    content = models.TextField(_('content'))
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Modèle de chatbot
class QAPair(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField(blank=True, null=True)

def __str__(self):
        return self.question

def save(self, *args, **kwargs):
        if not self.answer:
            self.answer = self.fetch_transformer_answer(self.question)
        super().save(*args, **kwargs)

@staticmethod
def load_knowledge_base():
        # Construire le chemin d'accès absolu au fichier JSON
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, 'knowledge_base.json')
        with open(file_path, 'r', encoding='utf-8') as file:
            knowledge_base = json.load(file)
        return knowledge_base

@staticmethod
def fetch_transformer_answer(question):
        knowledge_base = load_knowledge_base()
        context = ""
        for article in knowledge_base:
            if article['topic'].lower() in question.lower():
                context = article['content']
                break

        if not context:
            context = "Je ne trouve pas d'informations pertinentes sur ce sujet."

        qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
        result = qa_pipeline(question=question, context=context)
        answer = result['answer'].strip()
        return answer

def find_best_answer(question, qa_pairs):
    questions = [qa.question for qa in qa_pairs]
    questions.append(question)

    tv = TfidfVectorizer()
    tf = tv.fit_transform(questions)
    values = cosine_similarity(tf[-1], tf[:-1])

    best_match_index = int(np.argmax(values[0]))  # Convertir en entier Python natif
    best_match_score = values[0, best_match_index]

    if best_match_score > 0.3:  # Ajustez ce seuil selon vos besoins
        return qa_pairs[best_match_index].answer
    return fetch_transformer_answer(question)  # Appel au modèle local pour une réponse dynamique
