import scipy.io
import os

# Watch-N-Patch 25 Joints
WATCH_N_PATCH_JOINTS = ['SpineBase', 'SpineMid', 'Neck', 'Head',
                        'ShoulderLeft', 'ElbowLeft', 'WristLeft', 'HandLeft',
                        'ShoulderRight', 'ElbowRight', 'WristRight', 'HandRight',
                        'HipLeft', 'KneeLeft', 'AnkleLeft', 'FootLeft',
                        'HipRight', 'KneeRight', 'AnkleRight', 'FootRight',
                        'SpineShoulder',
                        'HandTipLeft', 'ThumbLeft', 'HandTipRight', 'ThumbRight']

# Setting up group of joints for visualization purpose
JOINTS_SPLIT = {'Spine': [0, 1, 20], 'Head': [2, 3],
                'Upper': [4, 5, 6, 8, 9, 10], 'Hands': [7, 11, 21, 22, 23, 24],
                'Bottom': [12, 13, 14, 15, 16, 17, 18, 19]}

def get_joints(data_path: str):
    """
    :param
        data_path : str
            path to watch-n-patch .mat file
    :return
        joints : dict
            dictionary with frame_path as key and joints annotation as value
    """
    joints = dict()
    body = scipy.io.loadmat(os.path.join(data_path, 'body.mat'))['body']

    # Watch-n-patch save depth images on \depth folder, if you're on unix system change the path format
    DEPTH = os.path.join(data_path, 'depth')
    names = get_image_name(DEPTH)
    for frame in range(len(body)):
        for k in range(6):
            if body[frame][k]['isBodyTracked'] == 1:
                joint_tracked = body[frame][k]['joints']
                joints[os.path.join(data_path, 'depth', names[frame])] = dict()
                for i in range(len(joint_tracked[0][0][0])):
                    # Joint not tracked are set as not visible, using (-1, -1) as coordinates
                    if joint_tracked[0][0][0][i]['trackingState'][0][0][0][0] == 0:
                        joints[os.path.join(data_path, 'depth', names[frame])][i] = (-1, -1)
                    else:
                        # Getting joint annotations
                        for j in joint_tracked[0][0][0][i]['depth'][0]:
                            x = j[0][0]
                            y = j[1][0]
                            joints[os.path.join(data_path, 'depth', names[frame])][i] = (round(x), round(y))
                break
    return joints


def get_joints_rgb(data_path: str):
    """
    :param
        data_path : str
            path to watch-n-patch .jpg file
    :return
        joints : dict
            dictionary with frame_path as key and joints annotation as value
    """
    joints = dict()
    body = scipy.io.loadmat(os.path.join(data_path, 'body.mat'))['body']

    # Watch-n-patch save depth images on \depth folder, if you're on unix system change the path format
    DEPTH = os.path.join(data_path, 'rgbjpg')
    names = get_image_name(DEPTH)
    for frame in range(len(body)):
        for k in range(6):
            if body[frame][k]['isBodyTracked'] == 1:
                joint_tracked = body[frame][k]['joints']
                joints[os.path.join(data_path, 'rgbjpg', names[frame])] = dict()
                for i in range(len(joint_tracked[0][0][0])):
                    # Joint not tracked are set as not visible, using (-1, -1) as coordinates
                    if joint_tracked[0][0][0][i]['trackingState'][0][0][0][0] == 0:
                        joints[os.path.join(data_path, 'rgbjpg', names[frame])][i] = (-1, -1)
                    else:
                        # Getting joint annotations
                        for j in joint_tracked[0][0][0][i]['color'][0]:
                            x = j[0][0]
                            y = j[1][0]
                            joints[os.path.join(data_path, 'rgbjpg', names[frame])][i] = (round(x), round(y))
                break
    return joints


def get_image_name(img_dir: str):
    images = os.listdir(img_dir)
    images.sort()
    if any(".DS_Store" in s for s in images):
        images.remove(".DS_Store")
    if any("._.DS_Store" in s for s in images):
        images.remove("._.DS_Store")
    return images