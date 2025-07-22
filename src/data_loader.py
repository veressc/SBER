import os
import pandas as pd
from typing import List


def load_annotations(annotation_dir: str) -> pd.DataFrame:
    records: List[dict] = []
    for fname in os.listdir(annotation_dir):
        if not fname.endswith('.out'):
            continue
        doc_id = os.path.splitext(fname)[0]
        path = os.path.join(annotation_dir, fname)
        with open(path, encoding='utf-8') as f:

            lines = [L.strip() for L in f if L.strip()]

        if lines and (lines[0] == doc_id or lines[0] == doc_id.split('_')[-1]):
            lines = lines[1:]
        for line in lines:

            line = line.replace('\t', ' ')

            tokens = line.split()
            if len(tokens) < 4:
                continue

            lemma, ent_type, canonical = tokens[-3:]

            surface = " ".join(tokens[:-3])
            records.append({
                'document_id': doc_id,
                'entity': ent_type,
                'gold_answer': surface
            })
    return pd.DataFrame(records)


def load_texts(text_dir: str, skip_lines: int = 4) -> pd.DataFrame:
    records: List[dict] = []
    for fname in os.listdir(text_dir):
        if not fname.endswith('.txt'):
            continue
        doc_id = os.path.splitext(fname)[0]
        path = os.path.join(text_dir, fname)
        with open(path, encoding='utf-8') as f:
            lines = f.read().splitlines()
        body = "\n".join(lines[skip_lines:]).strip()
        records.append({
            'document_id': doc_id,
            'document_text': body
        })
    return pd.DataFrame(records)
