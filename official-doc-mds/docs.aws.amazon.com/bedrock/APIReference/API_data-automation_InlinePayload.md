

# InlinePayload
<a name="API_data-automation_InlinePayload"></a>

Inline payload for ingestion jobs.

## Contents
<a name="API_data-automation_InlinePayload_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** deleteEntitiesInfo **   <a name="bedrock-Type-data-automation_InlinePayload-deleteEntitiesInfo"></a>
Information about entities to delete.  
Type: [DeleteEntitiesInfo](API_data-automation_DeleteEntitiesInfo.md) object  
Required: No

 ** upsertEntitiesInfo **   <a name="bedrock-Type-data-automation_InlinePayload-upsertEntitiesInfo"></a>
Information about entities to upsert.  
Type: Array of [UpsertEntityInfo](API_data-automation_UpsertEntityInfo.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: No

## See Also
<a name="API_data-automation_InlinePayload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/InlinePayload) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/InlinePayload) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/InlinePayload) 