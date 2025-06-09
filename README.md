# GSOPs 2.5 (Gaussian Splatting Operators) for SideFX Houdini 20.5
_Now available under the **Houdini Commercial** license._

[Watch the GSOPs 2.5 Sizzle Reel](https://youtu.be/9GcNrg5zAKk)

[Watch the GSOPs Showcase](https://www.youtube.com/watch?v=5V7mBuVxlt4)

[How to Install](https://github.com/david-rhodes/GSOPs?tab=readme-ov-file#installation)

[![GSOPs Showcase Video](help/images/gsops_pig.gif)](https://www.youtube.com/watch?v=5V7mBuVxlt4)

## About
GSOPs is a collaborative project from [David Rhodes](https://www.linkedin.com/in/davidarhodes/) and [Ruben Diaz](https://www.linkedin.com/in/rubendz/). It is comprised of a [viewport renderer](https://github.com/rubendhz/houdini-gsplat-renderer), [example files](https://github.com/david-rhodes/GSOPs/tree/develop/hip), and several digital assets to assist with common I/O and editing operations for 3DGS content. GSOPs is developed in our personal time and is provided as-is. 

Use GSOPs to import, render, edit, and export 3D Gaussian splatting models, or to generate synthetic training data. Synthetic data is capable of producing high-fidelity models with view-dependent effects and performant rendering on most modern devices. GSOPs is effective at isolating objects, eliminating noise and floaters, deforming and animating splat models, composing scenes, meshing and relighting splats, and conducting feature analysis.

For more examples of GSOPs in action, check out [GSOPs on LinkedIn](https://www.linkedin.com/feed/hashtag/?keywords=gsops) and [GSOPs on YouTube](https://www.youtube.com/playlist?list=PLBC-5xO_PccbefAB35xGOmAmWFRXLPDCo).

**🥉 GSOPs won 3rd place in the [H20 SIDEFX LABS Tech Art Challenge](https://www.sidefx.com/community-main-menu/contests-jams/h20-tech-art-challenge/).**

[Join us on Discord!](https://discord.gg/bwsvvRYNJa)

![GSplat Source](/help/images/gsplat_source_example.png)

## Motivation
Houdini's powerful, data-efficient architecture makes it the go-to platform for procedural content production across many industries. Its flexible and extensible design empowers users to tackle complex challenges at the right level of abstraction, focusing on problem-solving rather than low-level technicalities.

This unique combination of flexibility and ease of use is especially valuable in the rapidly evolving field of Novel View Synthesis. It enables quick prototyping, testing, and refinement of new workflows, keeping pace with the latest research. Additionally, it provides a direct path for innovations to transition into real-world applications within a well-established, production-ready solution.

SideFX, the developer of Houdini, fosters innovation through its "Labs" initiative. This incubator allows for the iteration of new tools and workflows before they become mainstream. Similarly, GSOPs provides a dedicated playground for Novel View Synthesis, enabling users to craft new workflows that closely align with the final visual result while prioritizing a creative and enjoyable process.

## Support Us
**We're passionate about the potential of editable radiance fields in SideFX Houdini and we're eager to continue pushing boundaries. If you believe in this initiative or have benefitted from GSOPs, please consider supporting us. Thank you!**

<a href="https://www.buymeacoffee.com/gsopsproject"><img src="help/images/support_gsops.png" alt="Support GSOPs" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

## Installation
1. Clone this repository (use the `develop` branch for the latest and greatest).
    * **[Using Git CLI]** Clone **recursively** with `--recurse-submodules`, **OR** run `git submodule init` followed by `git submodule update`.
    * **[Using [GitHub Desktop](https://desktop.github.com/download/)]** Clone repository with URL: `https://github.com/david-rhodes/GSOPs.git` (submodules will automatically be initialized).
2. Install and configure the GSOPs Houdini package by opening the `hip/gsops_installer.hip` file in Houdini, selecting the `INSTALL_GSOPS` node and clicking `INSTALL`. Feel free to also click the "RETRIEVE SAMPLE DATA" button to download sample Gaussian Splat models (these are used in the example hip files provided).

   <img width="548" alt="419229706-0c526dae-0ed9-4ab0-b986-9924f29c1481" src="https://github.com/user-attachments/assets/a0a08d0a-f6ea-491b-9419-a2e9e0fc706b" />
3. **[Optional]** Install the latest SideFX Labs release.


## Getting Started
1. Open a few example scenes from the `hip` directory. Use these to validate your installation and better understand Gaussian splatting workflows.
2. For accurate color results, [disable OpenColorIO in the viewport](https://vimeo.com/1001396463). If you don't see your splats in the viewport, you may also need to disable viewport lighting.
3. The `Gaussian Splats Source` SOP (i.e., the "render" node) does not currently have an output. This means it must exist at the end of your network. (We intend to change this in the future so that it's embedded in the `gaussian_splats_import` SOP for a streamlined user experience.)
4. Houdini provides many wonderful tools that will help you work with Gaussian Splat data. If you're not already familiar, check out the following SOP nodes: point cloud normal/surface, VDB from particles/polygons, cluster, and group (w/keep in bounding regions).

## Breaking Changes in GSOPs 2.5
With GSOPs 2.5, spherical harmonics have been refactored to streamline data access and support SH rotation (and other editing operations). When Gaussian splats are imported, `f_rest_*` attributes are converted to a vector array named `sh_coefficients`. The following nodes are affected:
* **[v2.0]** `gaussian_splats_import` 
* **[v3.0]** `gaussian_splats_export`
* **[v1.0]** `gaussian_splats_source` _(This is not necessarily a breaking change, but the old `GSplat Source` SOP has been hidden. It is **strongly** recommended to use this node for future compatibility!)_

**To avoid introducing undesired modifications to existing scenes, do not blindly update instances of the import and export nodes!** (Node updates should be opt-in because the type definition version has been incremeneted.)

## Notes
* Please be kind. We love innovating and learning, and we want you to benefit from this project.
* GSOPs is only supported for Houdini 20.5. This is due to an API change in the HDK. You should still be able to customize your installation for Houdini 20.0 and continue using the digital assets.
* We provide precompiled binaries of [`houdini-gsplat-renderer`](https://github.com/rubendhz/houdini-gsplat-renderer) for Houdini 20.5 on Windows and MacOS. Linux is not officially supported, but you can attempt to compile it yourself. 
* Please adhere to the [SideFX Houdini License Agreement](https://www.sidefx.com/legal/license-agreement/).
* GSOPs can generate Gaussian splat training data, but it cannot train models. If you want to train models locally, please see [3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://github.com/graphdeco-inria/gaussian-splatting) or [Postshot](https://www.jawset.com/).
* If you're interested in what you've seen and would like to discuss innovation/R&D collaboration opportunities, please contact us.

## GSOPs Nodes
<img src="/help/images/gsops_nodes.png" alt="drawing" width="300"/>

GSOPs is packed with features. For more information regarding any of the nodes shown above, please check the [wiki](https://github.com/david-rhodes/GSOPs/wiki/GSOPs-Nodes) and reference the built-in help cards.

## **[NEW]** Coarse Meshing
GSOPs 2.5 introduces dependency-free coarse meshing for 3D Gaussian Splatting. Coarse meshes are an effective "sparse node graph" for splat editing operations.

* [Coarse Meshing Utilities](https://github.com/david-rhodes/GSOPs/wiki/GSOPs-Nodes#coarse-meshing)
* [Coarse Meshing Guidelines](https://github.com/david-rhodes/GSOPs/wiki/Coarse-Meshing-Guidelines)

## Splat Animation Sequences
* It's possible to export splat animation sequences (one .ply per file). You can load and render these in [Postshot](https://www.jawset.com/), [SuperSplat](https://playcanvas.com/supersplat/editor/), [Brush](https://github.com/ArthurBrussee/brush), and [Unity](https://github.com/david-rhodes/GSOPs/blob/develop/extra/UnityGaussianSplatting/INSTRUCTIONS.md).

## Synthetic Training Data
* You can use Houdini renders from procedural and manually generated camera poses (in COLMAP format) to convert your CG scenes to 3D Gaussian Splats. With GSOPs 2.0, png image support has been added to the `generate_training_data` SOP. This means you can train alpha-masked 3DGS models, producing cleaner reconstructions.
* The `gaussian_splats_generate_training_data` SOP has been updated in GSOPs 2.5 to support rendering in Karma and other 3rd party renderers. Previously, the render camera was constrained via Python, which caused evaluation issues in other Houdini contexts. The render camera is now constrained via channel expressions, avoiding this race condition. 

## Help
* All digital assets exist in the SOPS context and (most) have their own help card documentation.
* [Join us on Discord](https://discord.gg/bwsvvRYNJa).

## Known Issues
We consider GSOPs to be a professional-grade prototyping toolset. It is not free from error, and the user experience could be improved in many areas. Here are some of the known issues:

* **[FIXED]** ~~Rotating a splat model will not update spherical harmonics data accordingly. As a result, view-dependent lighting effects will not behave correctly in exported models.~~
* It is possible to create bad export data when using the `unpack` feature of `gaussian_splats_visualize_boxes`. As a workaround, avoid having this node in any data stream leading to an export node.
* The`gaussian_splats_feature_analysis` visualizer sometimes fails to refresh (toggle the visualize button as a workaround), and this often precedes a Houdini crash. The UX when dealing with very small or large attribute values also needs improvement.
* There's quite a bit of python in the project which needs additional error handling.

## Acknowledgements
Thank you, community! Your support, interest, and rapid contributions to gaussian splatting have inspired and motivated us.

### From David
[Jonne Geven](https://www.linkedin.com/in/jonne-geven/) and [Antti Veräjänkorva](https://www.linkedin.com/in/anttiv79/) have been my "rubber ducks." Thanks, guys. Always helpful to have cool people to bounce ideas around with.

[Aras Pranckevičius](https://aras-p.info) was quick to adopt Gaussian Splatting with a [Unity implementation](https://github.com/aras-p/UnityGaussianSplatting). He also went out of his way to help me with several problems I encountered during development. Thank you, Aras!

Major kudos to the original inventors of Gaussian Splatting, [Inria and the Max Planck Institut for Informatik (MPII)](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/)! 

### From Ruben 
I wouldn't have gotten this far without the inspiration from so many incredible open-source projects. While I haven’t directly reached out to the authors, their work has been immensely helpful, and I want to give special kudos to them:

- https://github.com/aras-p/UnityGaussianSplatting
- https://github.com/antimatter15/splat
- https://github.com/andrewwillmott/sh-lib

## Final Thoughts
This project is licensed under a _copyleft_ AGPL-3.0 license. If you require a different arrangement, please contact us to discuss alternatives.

Also, if you create something cool and share it on social media, we'd love to see. Please consider tagging us!

**Keep splatting!** 
