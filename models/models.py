
import models
from models import wrn
import torchvision.models as m


def get_model(args, classes, nc):
    # Load torchvision models with "torch_" prefix
    if 'torch' in args.model:
        return m.__dict__[args.model[6:]](num_classes=classes, pretrained=args.pretrained)

    # Load the pyramidnet used for autoaugment experiments on cifar
    if args.model == 'aa_PyramidNet':
        return models.__dict__[args.model](dataset='cifar10', depth=272, alpha=200, num_classes=classes)

    # Load the WideResNet-28-10
    if args.model == 'wrn':
        return wrn(num_classes=classes, depth=28, widen_factor=10, nc=nc)

    # Otherwise return models from other files
    return models.__dict__[args.model](num_classes=classes, nc=nc)
