import docx
import json

# extract each question and put it in a specific class:
# ART -> ARTICOLAZIONI
# OSS -> OSSA
# MUS -> MUSCOLI
def get_questions(filename):
    doc = docx.Document(filename)
    questions = []
    q_class = ""
    end_dot = ""
    for line in doc.paragraphs:
        if line.text[0] == ".":
            q_class = line.text[1:]
            continue
        ans = line.text[-1]
        if line.text[-3] != ".":
            end_dot = "."
        questions.append([line.text[:-1].rstrip()+end_dot, ans, q_class])
        end_dot = ""
    return questions

def export_to_json(data):
    l = [{"question": x[0], "answer": x[1], "class": x[2]} for x in data]
    with open("domande.json", "w") as f:
        json.dump(l, f)

if __name__ == "__main__":
    data = get_questions("../domande.docx")
    export_to_json(data)
