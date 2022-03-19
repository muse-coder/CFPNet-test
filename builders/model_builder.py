from model.CFPNet import CFPNet
import  model





def build_model(model_name, num_classes):
    if model_name == 'CFPNet':
        return CFPNet(classes=num_classes)
