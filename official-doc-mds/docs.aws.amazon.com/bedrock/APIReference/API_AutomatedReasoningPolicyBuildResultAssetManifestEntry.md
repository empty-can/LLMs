

# AutomatedReasoningPolicyBuildResultAssetManifestEntry
<a name="API_AutomatedReasoningPolicyBuildResultAssetManifestEntry"></a>

Represents a single entry in the asset manifest, describing one artifact produced by the build workflow.

## Contents
<a name="API_AutomatedReasoningPolicyBuildResultAssetManifestEntry_Contents"></a>

 ** assetType **   <a name="bedrock-Type-AutomatedReasoningPolicyBuildResultAssetManifestEntry-assetType"></a>
The type of asset (e.g., BUILD\_LOG, QUALITY\_REPORT, POLICY\_DEFINITION, GENERATED\_TEST\_CASES, POLICY\_SCENARIOS, FIDELITY\_REPORT, ASSET\_MANIFEST, SOURCE\_DOCUMENT).  
Type: String  
Valid Values: `BUILD_LOG | QUALITY_REPORT | POLICY_DEFINITION | GENERATED_TEST_CASES | POLICY_SCENARIOS | FIDELITY_REPORT | ASSET_MANIFEST | SOURCE_DOCUMENT`   
Required: Yes

 ** assetId **   <a name="bedrock-Type-AutomatedReasoningPolicyBuildResultAssetManifestEntry-assetId"></a>
A unique identifier for the asset, if applicable. Use this ID when requesting specific assets through the API.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 36.  
Pattern: `[0-9a-fA-F\-]+`   
Required: No

 ** assetName **   <a name="bedrock-Type-AutomatedReasoningPolicyBuildResultAssetManifestEntry-assetName"></a>
A human-readable name for the asset, if applicable. This helps identify specific documents or reports within the workflow results.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Required: No

## See Also
<a name="API_AutomatedReasoningPolicyBuildResultAssetManifestEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyBuildResultAssetManifestEntry) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyBuildResultAssetManifestEntry) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyBuildResultAssetManifestEntry) 