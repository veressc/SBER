def make_prompt(document_id: str, document_text: str, entity: str) -> str:
    prompt = (
        f"Документ «{document_id}»:\n\n"
        f"{document_text}\n\n"
        f"Пожалуйста, извлеки из этого текста все сущности типа «{entity}» "
        f"и верни их в виде списка (каждая сущность на новой строке)."
    )
    return prompt
