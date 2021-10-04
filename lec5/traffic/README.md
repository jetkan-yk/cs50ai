# Traffic

YouTube link: <https://youtu.be/9lazagweViE>

This is a summary of all different parameters that have been applied to my model.

In most cases, the model has the following structure:

1. Conv2D layer, ReLU activation
2. MaxPooling2D, 2x2 kernel
3. Hidden layer, ReLU activation, 0.5 dropout
4. Output layer, Softmax activation

Most of the effort was finding out the optimal configuration for the number of
filters in the 1st layer (Conv2D) and its kernel size. Here are my observations:

| Version | Conv2D configuration    | Training accuracy | Testing accuracy | Verdict                                                                           | Improvement                                              |
| ------- | ----------------------- | ----------------- | ---------------- | --------------------------------------------------------------------------------- | -------------------------------------------------------- |
| 1.0     | 32 filters, 3x3 kernel  | Average 0.05      | 0.05             | Model is not learning.                                                            | Increase number of filters.                              |
| 2.0     | 64 filters, 3x3 kernel  | Average 0.05      | 0.05             | Model is not learning.                                                            | Increase number of filters.                              |
| 3.0     | 128 filters, 3x3 kernel | Average 0.20      | 0.37             | Model is learning slowly, looks like we are heading toward the correct direction. | Increase number of filters.                              |
| 4.0     | 256 filters, 3x3 kernel | Average 0.05      | 0.05             | Model is not learning, looks like the model is underfitting.                      | Revert to 3.0 filters. Try experimenting on kernel size. |
| 5.0     | 128 filters, 4x4 kernel | Average 0.05      | 0.05             | Model is not learning, 4x4 kernel is worse than 3x3 kernel.                       | Try using odd numbers on kernel size.                    |
| 6.0     | 128 filters, 5x5 kernel | Average 0.80      | 0.92             | Works like a charm! Can we do better?                                             | Try using 6x6 kernel size.                               |
| 7.0     | 128 filters, 6x6 kernel | Average 0.77      | 0.91             | Seems like even number kernel size is not ideal.                                  | Try using 7x7 kernel size.                               |
| 8.0     | 128 filters, 7x7 kernel | Average 0.05      | 0.05             | Model is not learning, looks like the model is underfitting again.                | Can we do better?                                        |

After tweaking the number of filters and kernel size, I looked up the internet for research paper of the [top-1 ranked model in the German traffic sign benchmark](https://doi.org/10.1016/j.neunet.2018.01.005).
Their research concluded that the best model for the traffic sign problem has 3 Conv2D layers with local contrast normalisation and spatial transformation,
each applying a 2x2 MaxPooling 2D with ReLU activation. I tried to replicate their work by adjusting my model as such:

1. Conv2D layer, 200 filters, 7x7 kernel, ReLU activation
2. MaxPooling2D, 2x2 kernel
3. Conv2D layer, 250 filters, 4x4 kernel, ReLU activation
4. MaxPooling2D, 2x2 kernel
5. Hidden layer, 400 units, ReLU activation, 0.5 dropout
6. Output layer, Softmax activation

The final result is average 0.93 accuracy during training and 0.97 in testing.
