

# CreateDataset
<a name="API_CreateDataset"></a>

 Creates a new dataset resource asynchronously. Returns immediately with status CREATING. Poll `GetDataset` until status transitions to ACTIVE or CREATE\_FAILED. 

## Request Syntax
<a name="API_CreateDataset_RequestSyntax"></a>

```
POST /datasets HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "datasetName": "{{string}}",
   "description": "{{string}}",
   "kmsKeyArn": "{{string}}",
   "schemaType": "{{string}}",
   "source": { ... },
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateDataset_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateDataset_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateDataset_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateDataset-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [datasetName](#API_CreateDataset_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateDataset-request-datasetName"></a>
 Human-readable name for the dataset. Must be unique within the account. Immutable after creation.   
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: Yes

 ** [description](#API_CreateDataset_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateDataset-request-description"></a>
 A description of the dataset.   
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 200.  
Required: No

 ** [kmsKeyArn](#API_CreateDataset_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateDataset-request-kmsKeyArn"></a>
 Optional AWS KMS key ARN for server-side encryption on service Amazon S3 writes.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: No

 ** [schemaType](#API_CreateDataset_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateDataset-request-schemaType"></a>
 Versioned schema type governing the structure of examples. Immutable after creation.   
Type: String  
Valid Values: `AGENTCORE_EVALUATION_PREDEFINED_V1 | AGENTCORE_EVALUATION_SIMULATED_V1`   
Required: Yes

 ** [source](#API_CreateDataset_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateDataset-request-source"></a>
 Source of initial examples. Provide either inline examples or an S3 URI pointing to a JSONL file.   
Type: [DataSourceType](API_DataSourceType.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [tags](#API_CreateDataset_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateDataset-request-tags"></a>
 A map of tag keys and values to assign to the dataset.   
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

## Response Syntax
<a name="API_CreateDataset_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "createdAt": number,
   "datasetArn": "string",
   "datasetId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CreateDataset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CreateDataset_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateDataset-response-createdAt"></a>
 The timestamp when the dataset was created.   
Type: Timestamp

 ** [datasetArn](#API_CreateDataset_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateDataset-response-datasetArn"></a>
 The Amazon Resource Name (ARN) of the created dataset.   
Type: String  
Pattern: `arn:aws(-[a-z]+)*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:dataset/[a-zA-Z0-9_-]{1,110}` 

 ** [datasetId](#API_CreateDataset_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateDataset-response-datasetId"></a>
 The unique identifier of the created dataset.   
Type: String  
Pattern: `[a-zA-Z0-9_-]{1,110}` 

 ** [status](#API_CreateDataset_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateDataset-response-status"></a>
 Always CREATING immediately after this call. Poll `GetDataset` until status transitions to ACTIVE or CREATE\_FAILED.   
Type: String  
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED` 

## Errors
<a name="API_CreateDataset_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
This exception is thrown when a request is denied per access permissions  
HTTP Status Code: 403

 ** ConflictException **   
This exception is thrown when there is a conflict performing an operation  
HTTP Status Code: 409

 ** InternalServerException **   
This exception is thrown if there was an unexpected error during processing of request  
HTTP Status Code: 500

 ** ServiceQuotaExceededException **   
This exception is thrown when a request is made beyond the service quota  
HTTP Status Code: 402

 ** ThrottlingException **   
This exception is thrown when the number of requests exceeds the limit  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_CreateDataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/CreateDataset) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/CreateDataset) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CreateDataset) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/CreateDataset) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CreateDataset) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/CreateDataset) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/CreateDataset) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/CreateDataset) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/CreateDataset) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CreateDataset) 