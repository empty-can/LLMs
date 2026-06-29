

# DatasetSummary
<a name="API_DatasetSummary"></a>

 Summary information about a dataset. 

## Contents
<a name="API_DatasetSummary_Contents"></a>

 ** createdAt **   <a name="bedrockagentcorecontrol-Type-DatasetSummary-createdAt"></a>
 The timestamp when the dataset was created.   
Type: Timestamp  
Required: Yes

 ** datasetArn **   <a name="bedrockagentcorecontrol-Type-DatasetSummary-datasetArn"></a>
 The Amazon Resource Name (ARN) of the dataset.   
Type: String  
Pattern: `arn:aws(-[a-z]+)*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:dataset/[a-zA-Z0-9_-]{1,110}`   
Required: Yes

 ** datasetId **   <a name="bedrockagentcorecontrol-Type-DatasetSummary-datasetId"></a>
 The unique identifier of the dataset.   
Type: String  
Pattern: `[a-zA-Z0-9_-]{1,110}`   
Required: Yes

 ** datasetName **   <a name="bedrockagentcorecontrol-Type-DatasetSummary-datasetName"></a>
 The name of the dataset.   
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: Yes

 ** exampleCount **   <a name="bedrockagentcorecontrol-Type-DatasetSummary-exampleCount"></a>
 The number of examples in the dataset.   
Type: Long  
Required: Yes

 ** schemaType **   <a name="bedrockagentcorecontrol-Type-DatasetSummary-schemaType"></a>
 The schema type of the dataset.   
Type: String  
Valid Values: `AGENTCORE_EVALUATION_PREDEFINED_V1 | AGENTCORE_EVALUATION_SIMULATED_V1`   
Required: Yes

 ** status **   <a name="bedrockagentcorecontrol-Type-DatasetSummary-status"></a>
 The current status of the dataset.   
Type: String  
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED`   
Required: Yes

 ** updatedAt **   <a name="bedrockagentcorecontrol-Type-DatasetSummary-updatedAt"></a>
 The timestamp when the dataset was last updated.   
Type: Timestamp  
Required: Yes

 ** description **   <a name="bedrockagentcorecontrol-Type-DatasetSummary-description"></a>
 The description of the dataset.   
Type: String  
Required: No

 ** draftStatus **   <a name="bedrockagentcorecontrol-Type-DatasetSummary-draftStatus"></a>
 Publish synchronization state. Only authoritative when status is ACTIVE.   
Type: String  
Valid Values: `MODIFIED | UNMODIFIED`   
Required: No

## See Also
<a name="API_DatasetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/DatasetSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/DatasetSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/DatasetSummary) 