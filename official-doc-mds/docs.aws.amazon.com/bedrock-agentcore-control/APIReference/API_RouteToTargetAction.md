

# RouteToTargetAction
<a name="API_RouteToTargetAction"></a>

An action that routes requests to a gateway target, either statically or with weighted traffic splitting.

## Contents
<a name="API_RouteToTargetAction_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** staticRoute **   <a name="bedrockagentcorecontrol-Type-RouteToTargetAction-staticRoute"></a>
A static route that sends all matching requests to a single target.  
Type: [StaticRoute](API_StaticRoute.md) object  
Required: No

 ** weightedRoute **   <a name="bedrockagentcorecontrol-Type-RouteToTargetAction-weightedRoute"></a>
A weighted route that splits traffic between multiple targets.  
Type: [WeightedRoute](API_WeightedRoute.md) object  
Required: No

## See Also
<a name="API_RouteToTargetAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/RouteToTargetAction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/RouteToTargetAction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/RouteToTargetAction) 