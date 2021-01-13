import os
import numpy as np
import watch_n_patch
import scipy
from torch.utils.data import Dataset
import cv2

PATCH = 'watch_n_patch'

OFFICE_SPLIT = ['data_03-58-25', 'data_03-25-32', 'data_02-32-08', 'data_03-05-15', 'data_11-11-59',
                'data_03-21-23', 'data_03-35-07', 'data_03-04-16', 'data_04-30-36', 'data_02-50-20']
KITCHEN_SPLIT = ['data_04-51-42', 'data_04-52-02', 'data_02-10-35', 'data_03-45-21', 'data_03-53-06',
                 'data_12-07-43', 'data_05-04-12', 'data_04-27-09', 'data_04-13-06', 'data_01-52-55']


class ComposedDataset(Dataset):
    def __init__(self, root_dir=None):
        """
        Args:
            root_dir (string): Directory with all the images.
            split (string): Split for custom Dataset
        """
        print("Loader started.")
        self.root_dir = root_dir
        self.P_ID = list()
        self.joints = dict()

        # Load Watch-n-patch
        print("Loading Watch-n-patch...")

        mat = scipy.io.loadmat(os.path.join(root_dir, PATCH, 'data_splits', 'kitchen_split.mat'))
        kitchen_splits = mat['test_name'][0]

        mat = scipy.io.loadmat(os.path.join(root_dir, PATCH, 'data_splits', 'office_split.mat'))
        office_splits = mat['test_name'][0]

        patch_joints = dict()
        for el in kitchen_splits:
            if el not in KITCHEN_SPLIT:
                continue
            patch_joints = {**patch_joints, **watch_n_patch.get_joints_rgb(os.path.join(root_dir, PATCH, "kitchen", el[0]))}
        for el in office_splits:
            if el not in OFFICE_SPLIT:
                continue
            patch_joints = {**patch_joints, **watch_n_patch.get_joints_rgb(os.path.join(root_dir, PATCH, "office", el[0]))}
        print("Done.")

        self.size = len(patch_joints)
        print(f"{self.size} images loaded.\n")
        self.joints = {**patch_joints}


    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        name = list(self.joints.keys())[idx]

        img = cv2.imread(name)
        img = cv2.resize(img, None, fx=0.4, fy=0.4, interpolation=cv2.INTER_CUBIC)

        kpts = [i for i in self.joints[name].values()]
        kpts = np.array(kpts)
        kpts = kpts[np.newaxis, :]

        return img, kpts * 0.4, name

        # If you have no kpts, remember to return None as second element!
        # return img, None, name