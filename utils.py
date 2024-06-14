

def create_label_encoder(values):
    labels_to_code = {}
    for i, label in enumerate(sorted(values)):
        labels_to_code[label] = i
    code_to_labels = {code: label for label, code in labels_to_code.items()}
    return labels_to_code, code_to_labels