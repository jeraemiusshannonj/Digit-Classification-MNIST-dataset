random_idx=np.random.choice(len(x_test))
x_sample = x_test[random_idx]
y_true=np.argmax(y_test,axis=1)
y_sample_true=y_true[random_idx]
y_sample_pred_class=y_pred_classes[random_idx]

plt.title("Predicted {},True {}".format(y_sample_pred_class,y_sample_true),fontsize=16)
plt.imshow(x_sample.reshape(28,28),cmap='gray')
