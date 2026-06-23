from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "Qwen/Qwen3.5-2B"

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Load model safely (CPU stable mode)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map=None
)

model = model.to("cpu")

# Prompt
prompt = "Write a Python function to check if a number is prime"

inputs = tokenizer(prompt, return_tensors="pt")

# Generate (safe settings)
outputs = model.generate(
    **inputs,
    max_new_tokens=150,
    do_sample=False
)

# Print result
print(tokenizer.decode(outputs[0], skip_special_tokens=True))