# erAIser - Remove an object in video using AI
<p align="center"><img width="980" alt="첫슬라이드" src="https://user-images.githubusercontent.com/40483474/125912276-4d5b8952-7973-4884-80ff-93f475fb3bb8.PNG">
</p>

## Contents
1. [erAIser](#erAIser)
2. [Example](#Example)
3. [Demo screenshot](Demo-screenshot)
4. [Usage](#Usage)
    - Environment setup
    - Run demo
5. [References](#References)
6. [Contributors](#Contributors)

## erAIser 
<br>
‘erAIser’ is a service that provides a specific object erased video by using video object segmentation and video inpainting methods.
<br>

Most of video inpainting model need segmentation mask of objects. But it is hard to get in normal way. For your convenience, we used a deep learning model that allows users to easily obtain segmentation masks. Also, we combined this video object segmentation model with the video inpainting models to increase usability.

Our team consists of nine members of ‘Tobigs’ who are interested in computer vision task.

Let’s make your own video of a specific object being erased with ‘erAIser’!

<br>

## Example
<br>

<table>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/68596881/126003086-60641341-2845-4a26-94ac-de0132a46cd4.gif" width = 400 height = 300/></td><td><img src="https://user-images.githubusercontent.com/68596881/126003512-ca14ddd5-a54c-4299-801e-3de3378fd8d3.gif" width = 400 height = 300/></td>
  <tr>
</table>

<br>

## Demo screenshot
<br>
<p align="center"><img width="980" alt="front" src="https://user-images.githubusercontent.com/68596881/126006048-1625a188-5e9c-478d-9787-ff8d09c3039a.png">
</p>

<br>

## Usage
### Caution

- This `root` directory is for 'integrated demo(Siammask + VINet)'.
- If you want to use 'video object segmentation(Siammask)' model only, you should go `vos` directory and follow `readme.md`
- If you want to use 'video inpainting(VINet)' model only, you should go `vi` directory and follow `readme.md`

### Environment Setup
This code was tested in the following environments
 - Ubuntu 18.04.5
 - Python 3.7
 - Pytorch 1.8.1
 - CUDA 9.0
 - GCC 5.5 (gnu c++14 compiler)

If you don't use gnu c++14 compiler, then you will encounter CUDA build error  

1. Clone the repository & Setup

```bash
git clone https://github.com/shkim960520/tobigs-image-conference.git
cd tobigs-image-conference
conda create -n erAIser python=3.7 -y
conda activate erAIser
conda install cudatoolkit=9.0 -c pytorch -y
pip install -r requirements.txt
bash install.sh
```

2. Setup python path

```bash
export PYTHONPATH=$PWD:$PYTHONPATH
cd vos/
export PYTHONPATH=$PWD:$PYTHONPATH
cd ../vi/
export PYTHONPATH=$PWD:$PYTHONPATH
cd ../web/
export PYTHONPATH=$PWD:$PYTHONPATH
cd ../AANet/
export PYTHONPATH=$PWD:$PYTHONPATH
cd ../
```

### Demo

1. Setup your [environment](#Environment-setup)
2. Download the Deep Video Inpainting model

```bash
cd vi/results/vinet_agg_rec

file_id="1_v0MBUjWFLD28oMfsG6YwG_UFKmgZ8_7"
file_name="save_agg_rec_512.pth"
curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${file_id}" > /dev/null
code="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${code}&id=${file_id}" -o ${file_name}

file_id="12TRCSwixAo9AqyZ0zXufNKhxuHJWG-RV"
file_name="save_agg_rec.pth"
curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${file_id}" > /dev/null
code="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${code}&id=${file_id}" -o ${file_name}

cd ../../../
```
3. Download the Siammask model

```bash
wget http://www.robots.ox.ac.uk/~qwang/SiamMask_DAVIS.pth

file_id="1IKZWpMeWXq-9osBqG7e7bTABumIZ32gB"
file_name="checkpoint_e19.pth"
curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${file_id}" > /dev/null
code="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${code}&id=${file_id}" -o ${file_name}
```
4. Download the AANet model
```bash
cd AANet/
mkdir checkpoints
cd checkpoints/

file_id="1DT6_SZHTkmuEWvCfs07F2mGLSkgxYplo"
file_name="4dataset384.pth"
curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${file_id}" > /dev/null
code="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${code}&id=${file_id}" -o ${file_name}

cd ../../
```

5. Make `results` directory for saving result video
```bash
mkdir results
```
`results` is defualt setting. You can change this.

6-1. Run `inference.py` for erasing
```bash
python3 inference.py --resume checkpoint_e19.pth --config config_inference.json
```

6-2. Run `inference.py` for change people
```bash
python3 inference.py --resume SiamMask_DAVIS.pth --config config_inference.json --using_aanet True
```
The result video will be saved in `results`.

## References
- Wang, Qiang, et al. "Fast online object tracking and segmentation: A unifying approach." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2019.
- Wang, Tianyu, et al. "Instance shadow detection." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2020.
- Dahun Kim, Sanghyun Woo, Joon-Young Lee, and In So Kweon. Deep video inpainting. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pages 5792–5801, 2019.
- Siarohin, Aliaksandr and Woodford, et al. "Motion Representations for Articulated Animation." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2021.

## Contributors
<p align="center"><img width="980" alt="members" src="https://user-images.githubusercontent.com/68596881/126005946-f87fcf3a-5cb6-4e00-b4cd-6795ca349c62.png">
</p>
