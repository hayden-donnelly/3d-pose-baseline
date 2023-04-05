import keras 
from keras import layers

class Model(keras.Model):
    def __init__(
        self, 
        num_blocks, 
        num_sub_blocks, 
        num_keypoints, 
        dense_units, 
        dropout, 
        activation
    ):
        super().__init__()
        self.num_blocks = num_blocks
        self.num_sub_blocks = num_sub_blocks
        self.num_keypoints = num_keypoints
        self.dense_units = dense_units
        self.dropout = dropout
        self.activation = activation
        self.network = self.create_network()

    def create_network(self):
        inputs = layers.Input(shape=(self.num_keypoints, 2))
        x = layers.Dense(units = self.dense_units)(inputs)

        for i in range(self.num_blocks):
            res = x

            for j in range(self.num_sub_blocks):
                x = layers.Dense(units = self.dense_units)(inputs)
                x = layers.BatchNormalization()(x)
                x = layers.Activation(self.activation)(x)
                x = layers.Dropout(self.dropout)(x)

            x = res + x
        
        x = layers.Dense(units = self.num_keypoints * 3)(x)
        return keras.Model(inputs = inputs, outputs = x)
    
if __name__ == "__main__":
    model = Model(
        num_blocks = 2, 
        num_sub_blocks = 2, 
        num_keypoints = 17, 
        dense_units = 1024
    )
    model.network.summary()