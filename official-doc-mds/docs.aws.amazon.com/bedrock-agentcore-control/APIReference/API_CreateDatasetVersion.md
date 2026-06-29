

# CreateDatasetVersion
<a name="API_CreateDatasetVersion"></a>

 Publishes the current DRAFT as a new numbered version. The DRAFT is preserved and remains editable after publishing. Returns immediately with status UPDATING. Poll `GetDataset` until status transitions to ACTIVE or UPDATE\_FAILED. 

## Request Syntax
<a name="API_CreateDatasetVersion_RequestSyntax"></a>

```
POST /datasets/{{datasetId}}/versions HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateDatasetVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [datasetId](#API_CreateDatasetVersion_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateDatasetVersion-request-uri-datasetId"></a>
 The unique identifier of the dataset to publish a version for.   
Pattern: `[a-zA-Z0-9_-]{1,110}`   
Required: Yes

## Request Body
<a name="API_CreateDatasetVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateDatasetVersion_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateDatasetVersion-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

## Response Syntax
<a name="API_CreateDatasetVersion_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "createdAt": number,
   "datasetArn": "string",
   "datasetId": "string",
   "datasetVersion": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CreateDatasetVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CreateDatasetVersion_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateDatasetVersion-response-createdAt"></a>
 The timestamp when the version creation was initiated.   
Type: Timestamp

 ** [datasetArn](#API_CreateDatasetVersion_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateDatasetVersion-response-datasetArn"></a>
 The Amazon Resource Name (ARN) of the dataset.   
Type: String  
Pattern: `arn:aws(-[a-z]+)*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:dataset/[a-zA-Z0-9_-]{1,110}` 

 ** [datasetId](#API_CreateDatasetVersion_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateDatasetVersion-response-datasetId"></a>
 The unique identifier of the dataset.   
Type: String  
Pattern: `[a-zA-Z0-9_-]{1,110}` 

 ** [datasetVersion](#API_CreateDatasetVersion_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateDatasetVersion-response-datasetVersion"></a>
 The version number being created.   
Type: String  
Pattern: `(DRAFT|[0-9]+)` 

 ** [status](#API_CreateDatasetVersion_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateDatasetVersion-response-status"></a>
 Always UPDATING immediately after this call. Poll `GetDataset` until status transitions to ACTIVE or UPDATE\_FAILED.   
Type: String  
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED` 

## Errors
<a name="API_CreateDatasetVersion_Errors"></a>

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
<a name="API_CreateDatasetVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/CreateDatasetVersion) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/CreateDatasetVersion) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CreateDatasetVersion) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/CreateDatasetVersion) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CreateDatasetVersion) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/CreateDatasetVersion) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/CreateDatasetVersion) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/CreateDatasetVersion) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/CreateDatasetVersion) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CreateDatasetVersion) 