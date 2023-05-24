from transformers import pipeline

class Model:
    """Load model and predicting"""
	
	# 加载模型
    def __init__(self):
        self.question_answerer = pipeline("question-answering")
	
	# 预测
    def predict(self, question, context ):
        res = self.question_answerer(
            question = question,
            context = context
        )
     
        return res
