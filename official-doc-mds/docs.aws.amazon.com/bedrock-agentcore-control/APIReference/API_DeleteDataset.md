

# DeleteDataset
<a name="API_DeleteDataset"></a>

 Deletes a dataset version or an entire dataset asynchronously. If `datasetVersion` is absent, deletes all versions and the dataset record itself. If provided, deletes only that specific version. 

## Request Syntax
<a name="API_DeleteDataset_RequestSyntax"></a>

```
DELETE /datasets/{{datasetId}}?datasetVersion={{datasetVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteDataset_RequestParameters"></a>

The request uses the following URI parameters.

 ** [datasetId](#API_DeleteDataset_RequestSyntax) **   <a name="bedrockagentcorecontrol-DeleteDataset-request-uri-datasetId"></a>
 The unique identifier of the dataset to delete.   
Pattern: `[a-zA-Z0-9_-]{1,110}`   
Required: Yes

 ** [datasetVersion](#API_DeleteDataset_RequestSyntax) **   <a name="bedrockagentcorecontrol-DeleteDataset-request-uri-datasetVersion"></a>
 Optional version to delete. If absent, deletes the entire dataset. If provided, deletes only that specific version.   
Pattern: `(DRAFT|[0-9]+)` 

## Request Body
<a name="API_DeleteDataset_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteDataset_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "datasetArn": "string",
   "datasetId": "string",
   "datasetVersion": "string",
   "status": "string",
   "updatedAt": number
}
```

## Response Elements
<a name="API_DeleteDataset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [datasetArn](#API_DeleteDataset_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteDataset-response-datasetArn"></a>
 The Amazon Resource Name (ARN) of the dataset.   
Type: String  
Pattern: `arn:aws(-[a-z]+)*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:dataset/[a-zA-Z0-9_-]{1,110}` 

 ** [datasetId](#API_DeleteDataset_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteDataset-response-datasetId"></a>
 The unique identifier of the dataset.   
Type: String  
Pattern: `[a-zA-Z0-9_-]{1,110}` 

 ** [datasetVersion](#API_DeleteDataset_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteDataset-response-datasetVersion"></a>
 The version that was deleted.   
Type: String  
Pattern: `(DRAFT|[0-9]+)` 

 ** [status](#API_DeleteDataset_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteDataset-response-status"></a>
 The current status of the dataset after the delete request.   
Type: String  
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED` 

 ** [updatedAt](#API_DeleteDataset_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteDataset-response-updatedAt"></a>
 The timestamp when the delete was initiated.   
Type: Timestamp

## Errors
<a name="API_DeleteDataset_Errors"></a>

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
<a name="API_DeleteDataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/DeleteDataset) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/DeleteDataset) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/DeleteDataset) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/DeleteDataset) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/DeleteDataset) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/DeleteDataset) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/DeleteDataset) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/DeleteDataset) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/DeleteDataset) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/DeleteDataset) 