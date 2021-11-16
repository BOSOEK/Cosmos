# The enchanting Cosmos
Looking at the universe, one of the world's few wonders, I hope that busy modern people will think again about how to live in a dusty universe.
* Pytorch GAN Tutorial : [바로가기](https://pytorch.org/tutorials/beginner/dcgan_faces_tutorial.html)     
* Image source : Pixabay   
* Image count : 3612개   
* Data : [zip file](https://drive.google.com/file/d/1KcqJ2gIFPMW7s_U8B3a8Vn6VK77LF_93/view?usp=sharing)

<img width='400' src='https://user-images.githubusercontent.com/68007145/141922214-75448ed4-f476-429b-9100-b8d158dcb3cc.gif'>

## Introduce your work
When people think of the two words "space," they only think of the beautiful Milky Way or endless darkness. And they also decide on their own success and failure by dividing themselves into the successful life of the building owner and the failure of a simple part-time job. However, in the universe, there are not only galaxies that people consider beautiful, interstellar, and voids that people are afraid of, but also space dust that people take for granted, the sun and moon that people take for granted. As such, there are times when we are also beautiful and shiny like galaxies, and times when we are insignificant like dust in the universe, and sometimes we are lonely like emptiness. However, just as the sun is beautiful, it is the universe, and space dust is not trivial, neither our sparkling life nor messy life changes to other people's standards, but the absolute universe. Modern times are busy. Everyone just runs like crazy. In the process, we hope to realize once again through the universe we see from birth that not only the first place has succeeded, but that we are all beautiful and empty as a universe.

## Technology introduction
Images were created through the Hostile Generation Neural Network (GAN), and about 13,000 photos of the results of the "Space" search word have been crawled from Pixabay, a commercially available photo site, to build image datasets, of which 3,612 were selected.   
I knew that I had to proceed with the project as a GAN, but at the beginning of the project, I had no knowledge of GAN at all, so I had to start with studying GAN. In addition, when creating a generator and discriminator model, I got a sense by shoveling several times in layer selection.      
What I thought was the most important thing in this project was to make viewers think it was beautiful and fascinating, even if it was unrealistic, rather than realistic cosmic images. Therefore, when filtering out images, even cartoon images or images drawn by people other than real space photos are beautiful enough and added if they are related to the universe. And what influenced this point the most was Epochs, that is, the number of times of learning. If there are too many epochs, they are overfitting to create an image similar to the dataset I chose, but at this time, there were too many polar images (such as pictures, cartoons, and actual photos), so I often didn't think the result was space. Therefore, it was quite difficult to find an epoch that creates a cosmic image while writing down images of the dataset so that they would not appear. After more than 30 trials and errors, it was finally selected as 400 Epoch.

## A work of art
<img src='https://user-images.githubusercontent.com/68007145/141922830-55bb5d9d-963c-4171-8304-8d471d43c93e.png'>