import argparse

from datasets import load_dataset
from transformers import (
    BertForSequenceClassification,
    BertTokenizer,
    Trainer,
    TrainingArguments,
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--train_data", type=str)
    parser.add_argument("--output_dir", type=str)
    args = parser.parse_args()

    # Load dataset
    dataset = load_dataset("json", data_files={"train": args.train_data}, split="train")

    # Tokenize query-document pairs
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    def tokenize(example):
        return tokenizer(example["query"], example["document"], truncation=True, padding="max_length")
    dataset = dataset.map(tokenize, batched=True)

    # Load model
    model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)

    # Training arguments
    training_args = TrainingArguments(
        output_dir=args.output_dir,
        evaluation_strategy="epoch",
        per_device_train_batch_size=16,
        num_train_epochs=3,
        save_steps=500,
        logging_dir="./logs"
    )

    # Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset
    )

    trainer.train()
    trainer.save_model(args.output_dir)

if __name__ == "__main__":
    main()
