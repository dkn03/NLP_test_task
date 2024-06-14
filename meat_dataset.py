from torch.utils.data import Dataset

class MeatDataset(Dataset):

    def __init__(self, df, tokenizer, label_encoder):
        self.x = df['text']
        self.y = df['mtype']
        self.tokenizer = tokenizer
        self.label_encoder = label_encoder
    
    def __getitem__(self, index):
        item = dict(self.tokenizer(self.x[index], truncation=True, padding='max_length', max_length=512))
        item['label'] = self.label_encoder[self.y[index]]
        #item['label'] = self.tokenizer(self.y[index], truncation=True, padding='max_length', max_length=512)['input_ids']
        return item
        
    def __len__(self):
        return len(self.x)