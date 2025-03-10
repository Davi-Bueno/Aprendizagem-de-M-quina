import streamlit as st

def process_text(frase):
    char_count = len(frase)
    words = frase.split()
    word_count = len(words)
    longest_word = max(words, key=len) if words else ""
    reversed_chars = frase[::-1]
    reversed_words = " ".join(words[::-1])
    uppercase_text = frase.upper()
    lowercase_text = frase.lower()
    words_tuple = tuple(words)
    
    return {
        "char_count": char_count,
        "word_count": word_count,
        "longest_word": longest_word,
        "reversed_chars": reversed_chars,
        "reversed_words": reversed_words,
        "uppercase_text": uppercase_text,
        "lowercase_text": lowercase_text,
        "words_tuple": words_tuple,
    }

st.title("Analisador de Frases")

frase = st.text_input("Digite uma frase:")

if st.button("Analisar"):
    if frase:
        results = process_text(frase)
        
        st.write(f"**Número de caracteres:** {results['char_count']}")
        st.write(f"**Número de palavras:** {results['word_count']}")
        st.write(f"**Maior palavra:** {results['longest_word']}")
        st.write(f"**Frase invertida (por caracteres):** {results['reversed_chars']}")
        st.write(f"**Frase invertida (por palavras):** {results['reversed_words']}")
        st.write(f"**Frase em maiúsculas:** {results['uppercase_text']}")
        st.write(f"**Frase em minúsculas:** {results['lowercase_text']}")
        st.write(f"**Tupla de palavras:** {results['words_tuple']}")
    else:
        st.warning("Por favor, insira uma frase antes de analisar.")
