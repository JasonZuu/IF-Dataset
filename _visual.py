"""
Code used for get samples of data
"""

import numpy as np
import cv2

def _get_row(imgs)->np.ndarray:
    for i_img in range(len(imgs)):
        img = imgs[i_img]
        if i_img == 0:
            row = img
        else:
            row = np.concatenate((row, img), axis=1)
    return row


def visual_face(img_paths:list, nrow=4):
    vis_result = None
    row_imgs = []
    for i_img in range(1, len(img_paths)+1):
        img_path = img_paths[i_img-1]
        img = cv2.imread(img_path)
        img = cv2.resize(img, (224, 224))
        row_imgs.append(img)
        if i_img % nrow == 0 and i_img != 0:
            row = _get_row(row_imgs)
            row_imgs = []
            if vis_result is None:
                vis_result = row
            else:
                vis_result = np.concatenate((vis_result, row), axis=0)
    return vis_result

relevant_faces = ["samples/r1.png",
                    "samples/r2.png",
                    "samples/r3.png",
                    "samples/r4.png"]

irrelevant_faces = ["samples/ir1.png",
                    "samples/ir2.png",
                    "samples/ir3.png",
                    "samples/ir4.png"]

if __name__ == "__main__":
    # set path
    relevant_path = "imgs/relevant_sample.jpg"
    irrelevant_path = "imgs/irrelevant_sample.jpg"
    # get visual result
    relevant_vis = visual_face(relevant_faces)
    irrelevant_vis = visual_face(irrelevant_faces)
    # write out result
    cv2.imwrite(relevant_path, relevant_vis)
    cv2.imwrite(irrelevant_path, irrelevant_vis)
        
            