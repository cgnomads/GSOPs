# GSOPs 2.6 (Gaussian Splatting Operators) for SideFX Houdini 20.5

[Watch the GSOPs 2.5 Sizzle Reel](https://youtu.be/-_gqsi6NYcY)

[Watch the GSOPs Showcase](https://youtu.be/XZUUATb1u28)

[How to Install](https://github.com/cgnomads/GSOPs?tab=readme-ov-file#installation)

[![GSOPs Showcase Video](help/images/gsops_pig.gif)](https://www.youtube.com/watch?v=5V7mBuVxlt4)

## Upgrade Guide for Existing Users
**Our licensing options have changed.** [Learn more](https://www.cgnomads.com/licensing).

As a part of our transition to [CG Nomads](http://www.cgnomads.com), we have removed the renderer submodule dependency and decoupled example data from the repository to reduce its size, improve maintainability, and streamline installation. Therefore, we recommend you perform a fresh clone and follow the [installation instructions](https://github.com/cgnomads/GSOPs?tab=readme-ov-file#installation) as normal.

## Where Magic Meets Reality
Add ✨ to your Gaussian splatting scenes with GSOPs — the most versatile Gaussian Splats editing toolset!

Gaussian splatting is a radiance field technology that turns photos and videos into high-quality 3D content with view-dependent effects and fast rendering. Gaussian Splatting Operators (GSOPs) is a plug-in for SideFX Houdini that grants artists total creative control over Gaussian splatting scenes.

GSOPs includes a real-time viewport renderer, [example files](https://github.com/cgnomads/GSOPs/tree/develop/hip), and a suite of digital assets for efficient import, editing, and export of 2D and 3D Gaussian splatting content.

Among its many capabilities, GSOPs is effective at isolating objects, eliminating noise and "floaters", deforming and animating splat models, composing scenes, meshing and relighting, performing feature analysis, and generating synthetic training data capable of delivering high-fidelity results with complex view-dependent effects.

Developed by [David Rhodes](https://www.linkedin.com/in/davidarhodes/) and [Ruben Diaz](https://www.linkedin.com/in/rubendz/), GSOPs is now hosted under [CG Nomads](http://www.cgnomads.com).

For more examples of GSOPs in action, check us out on [LinkedIn](https://www.linkedin.com/feed/hashtag/?keywords=gsops) and [YouTube](https://www.youtube.com/playlist?list=PLh6-L_XjgKCv7PwEivhQJqEOCfqiY6pKg).

🥉 GSOPs won 3rd place in the [H20 SIDEFX LABS Tech Art Challenge](https://www.sidefx.com/community-main-menu/contests-jams/h20-tech-art-challenge/).

💬 [Join us on Discord!](https://discord.gg/bwsvvRYNJa)

![GSplat Source](/help/images/gsplat_source_example.png)

## Motivation
Houdini's powerful, data-efficient architecture makes it the go-to platform for procedural content production across many industries. Its flexible and extensible design empowers users to tackle complex challenges at the right level of abstraction, focusing on problem-solving rather than low-level technicalities.

This unique combination of flexibility and ease of use is especially valuable in the rapidly evolving field of Novel View Synthesis. It enables quick prototyping, testing, and refinement of new workflows, keeping pace with the latest research. Additionally, it provides a direct path for innovations to transition into real-world applications within a well-established, production-ready solution.

SideFX, the developer of Houdini, fosters innovation through its "Labs" initiative. This incubator allows for the iteration of new tools and workflows before they become mainstream. Similarly, GSOPs provides a dedicated playground for Novel View Synthesis, enabling users to craft new workflows that closely align with the final visual result while prioritizing a creative and enjoyable process.

## Support Us
We're passionate about the potential of editable radiance fields in SideFX Houdini and we're eager to continue pushing boundaries. If you believe in this initiative or have benefitted from GSOPs, please consider becoming an Early Access supporter. 

As a token of our appreciation, you'll gain access to [exclusive content](https://github.com/cgnomads/GSOPs/wiki/Early-Access-Content) and new features.

<a href="https://www.buymeacoffee.com/gsopsproject"><img src="help/images/support_gsops.png" alt="Support GSOPs" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

## Studio Licenses
Need support, private modifications, or commercial usage? Custom site licenses tailored to your studio’s needs are available upon request. Contact us at gsops.project@gmail.com for more information.

## Installation
1. Clone this repository (use the `develop` branch for the latest and greatest).
    * **[Using Git CLI]** `git clone https://github.com/cgnomads/GSOPs`
    * **[Using [GitHub Desktop](https://desktop.github.com/download/)]** Clone repository with URL: `https://github.com/cgnomads/GSOPs.git`
2. Install and configure the GSOPs Houdini package by opening the `hip/gsops_installer.hip` file in Houdini, selecting the `INSTALL_GSOPS` node and clicking `INSTALL`.
   
    <img width="548" alt="419229706-0c526dae-0ed9-4ab0-b986-9924f29c1481" src="https://github.com/user-attachments/assets/a0a08d0a-f6ea-491b-9419-a2e9e0fc706b" />
    
3. The installer will ask if you want to download sample data. Select "Yes" if you're interested in exploring our example content (recommended).
4. **[Optional]** Install the latest SideFX Labs release.

### Early Access Supporters
Activate your license using the GSOPs shelf button.    

![GSOPs Shelf](/help/images/gsops_shelf.png)

## Getting Started
1. If you chose not to download sample data during installation, you should do that now via the GSOPs Shelf. 
2. Open a few example scenes from the `hip` directory. Use these to validate your installation and better understand Gaussian splatting workflows.
3. For accurate color results, [disable OpenColorIO in the viewport](https://vimeo.com/1001396463). 
4. Disable viewport lighting and enable smooth shading. The `Gaussian Splats Source` node has a "Set Viewport Settings" button for your convenience.
5. The `Gaussian Splats Source` SOP (i.e., the "render" node) does not currently have an output. This means it must exist at the end of your network.

## Notes
* Please be kind. We love innovating and learning, and we want you to benefit from this project.
* GSOPs is only supported for Houdini 20.5. 
* Linux is not officially supported.
* Please adhere to the [SideFX Houdini License Agreement](https://www.sidefx.com/legal/license-agreement/).
* GSOPs can generate Gaussian splat training data, but it **cannot** train models. If you want to train models locally, please see [3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://github.com/graphdeco-inria/gaussian-splatting), [Postshot](https://www.jawset.com/), or [Brush](https://github.com/ArthurBrussee/brush) (a great option for Mac users).
* If you're interested in what you've seen and would like to discuss innovation/R&D collaboration opportunities, please [contact us(https://www.cgnomads.com/about-us).
* GSOPs is developed in our personal time and is provided as-is. 

## GSOPs Nodes
<img src="/help/images/gsops_nodes.png" alt="drawing" width="300"/>

GSOPs is packed with features. For more information regarding any of the nodes shown above, please check the [wiki](https://github.com/cgnomads/GSOPs/wiki/GSOPs-Nodes) and reference the built-in help cards.

## [NEW] Support for 2DGS
The `Gaussian Splats Import` SOP now accepts [2DGS](https://github.com/hbb1/2d-gaussian-splatting) models!

## [NEW & EARLY ACCESS] Support for Solaris & Karma
We now provide a `Gaussian Splats Import` LOP node to simplify rendering and relighting Splats in Solaris. Additionally, the `Gaussian Splats Evaluate Spherical Harmonics` has been updated to bake spherical harmonics to the color attribute (`v@Cd`) for raytracing. Check out the `solaris.hip` example to learn more.

## Coarse Meshing
GSOPs 2.5 introduces dependency-free coarse meshing for 3D Gaussian Splatting. Coarse meshes are an effective "sparse node graph" for splat editing operations.

* [Coarse Meshing Utilities](https://github.com/cgnomads/GSOPs/wiki/GSOPs-Nodes#coarse-meshing)
* [Coarse Meshing Guidelines](https://github.com/cgnomads/GSOPs/wiki/Coarse-Meshing-Guidelines)

## Splat Animation Sequences
* It's possible to create, import, edit, and export splat animation sequences (one .ply per file). You can load and render these in [Postshot](https://www.jawset.com/), [SuperSplat](https://playcanvas.com/supersplat/editor/), [Brush](https://github.com/ArthurBrussee/brush), and [Unity](https://github.com/cgnomads/GSOPs/blob/develop/extra/UnityGaussianSplatting/INSTRUCTIONS.md).

## Synthetic Training Data
* You can use Houdini renders from procedural and manually generated camera poses (in COLMAP format) to convert your CG scenes to 3D Gaussian Splats. The `generate_training_data` SOP supports PNG image output, which enables the trainining of alpha-masked 3DGS models, which produces cleaner reconstructions.
* The `gaussian_splats_generate_training_data` SOP was updated in GSOPs 2.5 to support rendering in Karma and other 3rd party renderers. Previously, the render camera was constrained via Python, which caused evaluation issues in other Houdini contexts. The render camera is now constrained via channel expressions, avoiding this race condition. 

## Help
* Most digital assets exist in the SOPS context and (most) have their own help card documentation.
* [Join us on Discord](https://discord.gg/bwsvvRYNJa).

## Acknowledgements
Thank you, community! Your support, interest, and rapid contributions to Gaussian splatting have inspired and motivated us.

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