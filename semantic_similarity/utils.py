import os
import json
import jinja2
import numpy as np
import pandas as pd
from IPython.core.display import display, HTML
from gensim.parsing.preprocessing import (
    preprocess_string,
    strip_tags,
    strip_punctuation,
    strip_multiple_whitespaces,
    strip_numeric,
    remove_stopwords,
    strip_short
)


PREPROCESSING = [
    strip_tags,
    strip_punctuation,
    strip_multiple_whitespaces,
    strip_numeric,
    remove_stopwords,
    strip_short,
    lambda x: x.lower(),
]


def process_doc(doc, tokenize=True):

    processed_doc = preprocess_string(doc, filters=PREPROCESSING)
    return processed_doc if tokenize else ' '.join(processed_doc)


def show_example(i, docs, p_transform_doc, knn):

    template = """
        <h2>Document:</h2>
        <p style="font-size:10pt">{{ doc }}</p>
        <h2>Suggestions:</h2>
        {{ suggestions }}
    """

    vec = p_transform_doc(docs[i])
    distances, idx = knn.kneighbors(vec[np.newaxis, :], return_distance=True)

    suggestions = {
        'text': [docs[i] for i in idx[0][1:]],
        'cosine': distances[0][1:]
    }

    rendered_template = jinja2.Template(template).render(
        doc=docs[i],
        suggestions=pd.DataFrame(suggestions).to_html(index=False)
    )

    display(HTML(rendered_template))
