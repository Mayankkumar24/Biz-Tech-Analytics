

######                             **Part 2 – Reasoning Based Answers**

 





**Q1:  Choosing the Right Approach.**

**Ans:** To detect whether a product is missing its label, I would use object detection. This is because we need to

&nbsp;    locate the label in the image and check whether it is present or not, not just classify the entire product.

&nbsp;    Detection allows us to draw bounding boxes around the label and verify its existence. If detection does not   

&nbsp;    work well, I would try image classification as a fallback by training a model on two classes:

&nbsp;   **“label present”** and **“label missing”**. If both fail, segmentation could be used to precisely highlight the label

&nbsp;    region, but it is more complex and costly.





**Q2:  Debugging a Poorly Performing Model.**

**Ans:** First, I would compare the training images with the new factory images to see if there is any

&nbsp;    difference in lighting, background, or camera angle. I would also visualize predictions on new images to

&nbsp;    understand what the model is getting wrong. Then I would check for overfitting by comparing

&nbsp;    training and validation accuracy. I would also review the labels to ensure they are correct and consistent. 

&nbsp;    Finally, I would try adding more diverse images from the factory to retrain the model.



**Q3:  Accuracy vs Real Risk.**

**Ans:** Accuracy is not the right metric in this case because missing a defective product is much more

&nbsp;    costly than falsely flagging a good one. Instead, I would focus on recall, especially for the defective

&nbsp;    class, because it measures how many defective products we correctly detect. I would also look at the 

&nbsp;    confusion matrix to see how many defects are being missed. In a safety or quality control system, it is 

&nbsp;    better to catch more defects even if it produces a few false alarms.



**Q4:  Annotation Edge Cases.**

**Ans:** Blurry or partially visible objects should usually be kept in the dataset because they represent

&nbsp;    real-world conditions. Factory cameras often capture imperfect images, so the model needs to learn how to 

&nbsp;    handle them. However, if an image is too unclear to label correctly, it should be removed to avoid confusing 

&nbsp;    the model. The trade-off is between data quality and realism. Keeping difficult examples improves robustness,

&nbsp;    but too many bad labels can hurt performance.

