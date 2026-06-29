

# UpdateDataset
<a name="API_UpdateDataset"></a>

 Updates a dataset's metadata. Synchronous operation. Only provided fields are updated; omitted fields remain unchanged. To modify dataset content, use `AddDatasetExamples`, `UpdateDatasetExamples`, or `DeleteDatasetExamples`. 

## Request Syntax
<a name="API_UpdateDataset_RequestSyntax"></a>

```
PUT /datasets/{{datasetId}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateDataset_RequestParameters"></a>

The request uses the following URI parameters.

 ** [datasetId](#API_UpdateDataset_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateDataset-request-uri-datasetId"></a>
 The unique identifier of the dataset to update.   
Pattern: `[a-zA-Z0-9_-]{1,110}`   
Required: Yes

## Request Body
<a name="API_UpdateDataset_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateDataset_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateDataset-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [description](#API_UpdateDataset_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateDataset-request-description"></a>
 The updated description for the dataset.   
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 200.  
Required: No

## Response Syntax
<a name="API_UpdateDataset_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "datasetArn": "string",
   "datasetId": "string",
   "updatedAt": number
}
```

## Response Elements
<a name="API_UpdateDataset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [datasetArn](#API_UpdateDataset_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateDataset-response-datasetArn"></a>
 The Amazon Resource Name (ARN) of the updated dataset.   
Type: String  
Pattern: `arn:aws(-[a-z]+)*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:dataset/[a-zA-Z0-9_-]{1,110}` 

 ** [datasetId](#API_UpdateDataset_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateDataset-response-datasetId"></a>
 The unique identifier of the updated dataset.   
Type: String  
Pattern: `[a-zA-Z0-9_-]{1,110}` 

 ** [updatedAt](#API_UpdateDataset_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateDataset-response-updatedAt"></a>
 The timestamp when the dataset was updated.   
Type: Timestamp

## Errors
<a name="API_UpdateDataset_Errors"></a>

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

 ** ResourceNotFoundException **   
This exception is thrown when a resource referenced by the operation does not exist  
HTTP Status Code: 404

 ** ThrottlingException **   
This exception is thrown when the number of requests exceeds the limit  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_UpdateDataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/UpdateDataset) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/UpdateDataset) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/UpdateDataset) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/UpdateDataset) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/UpdateDataset) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/UpdateDataset) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/UpdateDataset) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/UpdateDataset) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/UpdateDataset) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/UpdateDataset) 