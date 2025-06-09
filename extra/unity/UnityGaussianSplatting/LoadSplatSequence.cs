using UnityEngine;

namespace GaussianSplatting.Runtime
{
    public class LoadSplatSequence : MonoBehaviour
    {
        // Public variable for the directory path
        [SerializeField] private string splatAssetsDirectory = "Assets/GaussianAssets/Batch";

        private string[] assetPaths;
        private int currentAssetIndex = 0;

        // Reference to the GaussianSplatRenderer component
        private GaussianSplatRenderer splatRenderer;

        // Start is called before the first frame update
        void Start()
        {
            // Get the GaussianSplatRenderer component on the same GameObject
            splatRenderer = GetComponent<GaussianSplatRenderer>();

            if (splatRenderer == null)
            {
                Debug.LogError("GaussianSplatRenderer component not found.");
                return;
            }

            // Get all asset paths in the specified directory
            assetPaths = System.IO.Directory.GetFiles(splatAssetsDirectory, "*.asset");

            // Make sure there are assets to load
            if (assetPaths.Length > 0)
            {
                // Load the first asset
                LoadNextAsset();
            }
            else
            {
                Debug.LogError($"No assets found in the specified directory: {splatAssetsDirectory}");
            }
        }

        // Update is called once per frame
        void Update()
        {
            // Check if there are more assets to load
            if (currentAssetIndex < assetPaths.Length)
            {
                // Load the next asset each frame
                LoadNextAsset();
            }
        }

        // Load the next GaussianSplatAsset and set it to the m_Asset variable
        private void LoadNextAsset()
        {
            string assetPath = assetPaths[currentAssetIndex];
            //Debug.Log(assetPath);
            // Load the asset from the specified path
            GaussianSplatAsset splatAsset = UnityEditor.AssetDatabase.LoadAssetAtPath<GaussianSplatAsset>(assetPath);

            // Check if the asset is not null
            if (splatAsset != null)
            {
                // Set the loaded asset to the m_Asset variable in the GaussianSplatRenderer component
                splatRenderer.m_Asset = splatAsset;

                // Increment the index for the next frame
                currentAssetIndex++;

                // Reset index to 0 if it exceeds the array length
                if (currentAssetIndex >= assetPaths.Length)
                {
                    currentAssetIndex = 0;
                }
            }
            else
            {
                Debug.LogError($"Failed to load asset at path: {assetPath}");
            }
        }
    }
}