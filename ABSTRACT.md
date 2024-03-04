The authors of the **PAXRAY: A Projected dataset for the segmentation of Anatomical structures in X-RAY data** present a novel pipeline for generating annotations to assist the CXR (chest X-ray) domain by extracting information from more easily annotatable CTs (computed tomography scans). They provide a densely labeled fine-grained dataset for anatomy segmentation, encompassing both frontal and lateral views. The methodology leverages the consistency of anatomy across imaging domains, utilizing established models in the CT domain to generate annotations automatically. These annotations and corresponding images are then projected to 2D, mimicking the X-ray domain.

To exploit anatomical structures, the authors used a sophisticated automatic system for collecting and integrating human body structures from computed tomography data first fine-grained anatomy dataset. Their evaluation showed that methods using anatomical information significantly improved the visual support of radiologists' conclusions. Based on high-quality predictions in CT space, the authors displayed 92 individual anatomical marks structures which, including superclasses, lead to a total of 166 labels in both _side_ and _front_ view. All annotations on both the lateral and frontal views overlap because the authors view anatomical structures as 3D volume classes that can overlap along one dimension.

## Dataset description

Due to the immense difficulty of gathering precise pixel-wise annotations in the CXR domain, most datasets rely on either automatically parsed pathology labels or complete medical reports. In contrast, as the authors extract information from much easier to annotate CTs, they propose a novel pipeline for generating annotations assisting the CXR domain and provide a densely labeled fine-grained dataset for anatomy segmentation containing both frontal and lateral
views. Here, they leverage the consistency of anatomy between imaging domains to collect annotations from established models in the CT domain and then project these automatically generated annotations and images to 2D imitating the X-ray domain as shown below:

<img src="https://github.com/dataset-ninja/paxray/assets/120389559/e24cf551-321c-4972-ba64-c7c88e1da261" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">Dataset creation protocol. The authors of the dataset apply established 3D segmentation methods to generate comprehensive annotations of a CT dataset. Afterwards, the CTs and their labels are projected to 2D using post-processing techniques to emulate X-ray characteristics.</span>

The authors consider four super-categories: bones, lung, mediastinum, and sub-diaphragm. Each fine-grained class is assumed to be a subset of its parent class, for example, the segmentation of individual vertebrae and overall ribs within the bone structure. The rib annotation is expanded by discerning individual ribs, posterior, and anterior parts based on their center and horizontal inflection.

For lung annotation, the authors utilize the lung lobe segmentation model. Merging individual lobes results in the formation of lung halves. Pulmonary vessels and total lungs are then gathered through calculated thresholding and post-processing strategies.

For the mediastinum, the authors focus on the area between the lung halves. This area is segmented and split into superior and inferior along the 4th T-spine following medical definitions. Annotations for the heart, aorta, airways, and esophagus are extracted.
Regarding the sub-diaphragm, the authors consider the area below the diaphragm. This area is extracted from the soft tissue region segmented using the BCA, which is then split centrally into the left/right hemidiaphragm due to the absence of an anatomical indicator. Volumes with contradicting segmentations are ignored, and volumes with noticeable errors are manually removed.

<img src="https://github.com/dataset-ninja/paxray/assets/120389559/2ece1048-2614-43f2-8e98-ef754e366ca7" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">Examples of overlapping annotations in both lateral and frontal view of PAX-ray.</span>

In medical reports, the authors of the dataset note that medical observations are frequently associated with specific anatomical regions to denote their respective positions. Building upon the assumption of co-occurrence between diseases and anatomical regions within the text, a straightforward baseline is developed by the authors to assess the effectiveness of anatomy guidance in grounding observations.

For each image-report pair in a dataset comprising N pairs, the authors focus on the finding-section of the report. This section contains descriptions of visual observations present in the image. The authors process the report sentence-wise, segmenting it into medically relevant phrases. These phrases are then classified as either problems or treatments using a named-entity-recognition (NER) model. Any non-relevant information is subsequently discarded.

<img src="https://github.com/dataset-ninja/paxray/assets/120389559/601c2f43-926a-4ef8-9a57-33977cdd30dd" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">Examples of overlapping annotations in both lateral and frontal view of PAX-ray.</span>

The authors did not provide the resulting descriptions, so we cannot tag them.
