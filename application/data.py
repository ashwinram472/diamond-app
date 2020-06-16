from application.model import Diamonds
def data():
    diamondlist = Diamonds.objects.aggregate(*[
                {
                    '$group': {
                        '_id': {
                            '__alias_0': '$carat', 
                            '__alias_1': '$price', 
                            '__alias_2': '$shapeCode', 
                            '__alias_3': '$color', 
                            '__alias_4': '$clarity'
                        }
                    }
                }, {
                    '$project': {
                        '_id': 0, 
                        '__alias_0': '$_id.__alias_0', 
                        '__alias_1': '$_id.__alias_1', 
                        '__alias_2': '$_id.__alias_2', 
                        '__alias_3': '$_id.__alias_3', 
                        '__alias_4': '$_id.__alias_4'
                    }
                }, {
                    '$project': {
                        'x': '$__alias_0', 
                        'y': '$__alias_1', 
                        'shape': '$__alias_2', 
                        'color': '$__alias_3', 
                        'detail': '$__alias_4', 
                        '_id': 0
                    }
                }, {
                    '$limit': 10
                }
            ])
    return diamondlist