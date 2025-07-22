# src/data_loader.py

import os
import pandas as pd

def load_annotations(annotation_dir: str) -> pd.DataFrame:
    """
    Читает все .out-файлы из папки и возвращает DataFrame с колонками:
      - document_id  (например 'brexit_ru.txt_file_10')
      - entity       (тип сущности: PER, LOC, ORG, EVT…)
      - gold_answer  (строка surface_form из разметки)
    """
    records = []
    for fname in os.listdir(annotation_dir):
        if not fname.endswith('.out'):
            continue
        doc_id = os.path.splitext(fname)[0]
        path = os.path.join(annotation_dir, fname)
        with open(path, encoding='utf-8') as f:
            lines = [L.strip() for L in f if L.strip()]
        # Убираем, если первая строка внутри — просто ID
        if lines and lines[0] == doc_id.split('_')[-1]:
            lines = lines[1:]
        for line in lines:
            parts = line.split()
            if len(parts) >= 4:
                surface, lemma, ent_type, canonical = parts[:4]
                records.append({
                    'document_id': doc_id,
                    'entity': ent_type,
                    'gold_answer': surface
                })
    return pd.DataFrame(records)


def load_texts(text_dir: str, skip_lines: int = 4) -> pd.DataFrame:
    """
    Читает все .txt-файлы из папки, пропуская первые skip_lines строк (метаданные),
    и возвращает DataFrame с колонками:
      - document_id   (имя файла без .txt)
      - document_text (тело статьи с 5-й строки и дальше)
    """
    records = []
    for fname in os.listdir(text_dir):
        if not fname.endswith('.txt'):
            continue
        doc_id = os.path.splitext(fname)[0]
        path = os.path.join(text_dir, fname)
        with open(path, encoding='utf-8') as f:
            lines = f.read().splitlines()
        # Собираем текст, начиная с 5-й строки
        body = "\n".join(lines[skip_lines:]).strip()
        records.append({
            'document_id': doc_id,
            'document_text': body
        })
    return pd.DataFrame(records)
