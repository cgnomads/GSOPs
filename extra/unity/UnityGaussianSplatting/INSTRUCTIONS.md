To play and capture splat sequences in Unity, using one .ply file per frame, follow these steps:
1. Download and configure [Unity Gaussian Splatting](https://github.com/aras-p/UnityGaussianSplatting).
2. Replace `GaussianSplatAssetCreator.cs` in that project with the version in this directory. This replaces single splat file conversion with conversion of an entire directory of splat files.
3. Export a splat sequence from GSOPs in Houdini using `Frame Range` export mode in the `Gaussian Splats Export` node. 
4. Convert your exported splat sequence and place the converted assets into an asset subdirectory (e.g., `Assets/GaussianSplatAnimations/MySplatSequence`).
5. Add `LoadSplatSequence.cs` to the Unity 3DGS Playground project. 
6. Add `LoadSplatSequence` as a component to the `GaussianSplats` GameObject.
7. Set the `SplatAssetsDirectory` to the path from step 4. 
8. Play the game and watch your gaussian splatting animation.
9. Leverage Unity API's [ScreenCapture.CaptureScreenshot](https://docs.unity3d.com/ScriptReference/ScreenCapture.CaptureScreenshot.html) to "render" your animation.

<img src="https://raw.githubusercontent.com/david-rhodes/GSOPs/develop/help/images/unity_splat_sequences.png" title="Gaussian Splatting Unity Sequences." alt="Gaussian Splatting Unity Sequences info." width="1920">
