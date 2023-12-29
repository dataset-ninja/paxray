from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "PAXRAY"
PROJECT_NAME_FULL: str = (
    "PAXRAY: A Projected dataset for the segmentation of Anatomical structures in X-RAY data"
)
HIDE_DATASET = True  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.Unknown()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Industry.Medical()]
CATEGORY: Category = Category.Medical()

CV_TASKS: List[CVTask] = [CVTask.SemanticSegmentation()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.SemanticSegmentation()]

RELEASE_DATE: Optional[str] = None  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = 2022

HOMEPAGE_URL: str = "https://constantinseibold.github.io/paxray/"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 11893631
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/paxray"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[
    Union[str, dict]
] = "https://drive.google.com/drive/folders/1rzlsZ0bfByRMBoywOPWZW08GNgIwCU9P?usp=sharing"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = None
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

# If you have more than the one paper, put the most relatable link as the first element of the list
# Use dict key to specify name for a button
PAPER: Optional[Union[str, List[str], Dict[str, str]]] = {
    "Research Paper": "https://arxiv.org/abs/2210.03416",
    "Supplementary Material": "https://github.com/ConstantinSeibold/constantinseibold.github.io/blob/master/pdfs/0058_Supplementary_Camera_Ready.pdf",
}
BLOGPOST: Optional[Union[str, List[str], Dict[str, str]]] = None
REPOSITORY: Optional[Union[str, List[str], Dict[str, str]]] = None

CITATION_URL: Optional[str] = None
AUTHORS: Optional[List[str]] = [
    "Constantin Seibold",
    "Simon Reiss",
    "Saquib Sarfraz",
    "Matthias A. Fink",
    "Victoria Mayer",
    "Jan Sellner",
    "Moon Sung Kim",
    "Klaus H. Maier-Hein",
    "Jens Kleesiek",
    "Rainer Stiefelhagen",
]
AUTHORS_CONTACTS: Optional[List[str]] = [
    "constantin.seibold@kit.edu",
    "simon.reiss@kit.edu",
    "muhammad.sarfraz@kit.edu",
    "matthias.fink@uni-heidelberg.de",
    "victoria.mayer@med.uni-heidelberg.de",
    "j.sellner@dkfz-heidelberg.de",
    "moon-sung.kim@uk-essen.de",
    "k.maier-hein@dkfz-heidelberg.de",
    "jens.kleesiek@uk-essen.de",
    "rainer.stiefelhagen@kit.edu",
]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = "GE joint research group"
ORGANIZATION_URL: Optional[Union[str, List[str]]] = None

# Set '__PRETEXT__' or '__POSTTEXT__' as a key with string value to add custom text. e.g. SLYTAGSPLIT = {'__POSTTEXT__':'some text}
SLYTAGSPLIT: Optional[Dict[str, Union[List[str], str]]] = {
    "__PRETEXT__": "Additionally, the images have ***im_id*** and ***view*** tags. The ***view*** is determined ***frontal*** or ***lateral*** patient location"
}
TAGS: Optional[List[str]] = None


SECTION_EXPLORE_CUSTOM_DATASETS: Optional[List[str]] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "project_name_full": PROJECT_NAME_FULL or PROJECT_NAME,
        "hide_dataset": HIDE_DATASET,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["blog"] = BLOGPOST
    settings["repository"] = REPOSITORY
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["authors_contacts"] = AUTHORS_CONTACTS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    settings["explore_datasets"] = SECTION_EXPLORE_CUSTOM_DATASETS

    return settings
