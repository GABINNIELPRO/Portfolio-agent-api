def prepare_multimodal_context(results):
    parts = []
    for r in results:
        if r["type"] == "text":
            parts.append(f"[TEXT:{r['id']}]\n{r['content']}")
        elif r["type"] == "image":
            parts.append(f"[IMAGE:{r['id']}]\nDESCRIPTION:{r['content']}")
    return "\n\n".join(parts)