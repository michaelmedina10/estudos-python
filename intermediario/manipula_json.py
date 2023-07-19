import json

pessoa = {
    "nome": "Michael",
    "sobrenome": "Medina",
    "endereco": "AABC10"
}

with open('write_json_dump.json', 'w') as arquivo:
    json.dump(
        pessoa,
        arquivo,
        ensure_ascii=False,
        indent=2
    )