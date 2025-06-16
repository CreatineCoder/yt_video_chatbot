from huggingface_hub import HfApi

api = HfApi(token="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")
print(api.whoami())