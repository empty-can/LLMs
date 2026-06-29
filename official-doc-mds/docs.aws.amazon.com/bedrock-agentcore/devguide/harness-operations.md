

# Observability and cost controls
<a name="harness-operations"></a>

This page covers monitoring your harness, controlling execution costs, and managing resource tags.

## Observability
<a name="harness-observability"></a>

Every harness invocation automatically generates traces, logs, and metrics through [AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) in CloudWatch. Model calls, tool invocations, memory operations, shell commands: each step appears with timing and payload details. No extra configuration. Traces are available from the first invocation.

**Example**  
Traces, logs, and metrics flow to CloudWatch through the harness execution role. View them in the [AgentCore Observability dashboard](https://us-west-2.console.aws.amazon.com/cloudwatch/home?region=us-west-2#/gen-ai-observability/agent-core/agents), or query programmatically through the CloudWatch Logs and X-Ray APIs.  
Before you see traces, [enable Transaction Search in CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Enable-Lambda-TransactionSearch.html) (one-time per account). See [AgentCore Observability getting started](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-get-started.html) for setup details.

```
# Stream logs
agentcore logs --harness research-agent

# Filter
agentcore logs --harness research-agent --since 1h --level error

# List recent traces
agentcore traces list --harness research-agent

# Get a specific trace
agentcore traces get <trace-id> --harness research-agent
```

Learn more: [Observability overview](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) · [metrics](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-runtime-metrics.html) · [telemetry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-telemetry.html) 

## CloudTrail
<a name="harness-cloudtrail"></a>

Harness operations are logged to AWS CloudTrail as management events (control plane) and data events (data plane). In CloudTrail, harness resources appear under the `AWS::BedrockAgentCore::Runtime` resource type rather than a harness-specific type. Harness is a managed abstraction over AgentCore Runtime, and CloudTrail events reflect the underlying runtime resource for consistency.

All harness CloudTrail events use `resources.type` = `AWS::BedrockAgentCore::Runtime`. The event names are:
+  `CreateHarness`, `UpdateHarness`, `DeleteHarness`, `GetHarness`, `ListHarnesses` (management events)
+  `InvokeAgentRuntime`, `InvokeAgentRuntimeCommand` (data events)

**Note**  
Data plane operations appear as `InvokeAgentRuntime` and `InvokeAgentRuntimeCommand` in CloudTrail, matching the underlying Runtime API. The `resources.ARN` field contains the harness ARN for control plane events and the runtime ARN for data plane events.

## Control cost with limits
<a name="harness-limits"></a>

Set hard caps so a runaway agent can’t burn through resources:
+  ** `maxIterations` ** - reasoning/action cycles per invocation. Default 75.
+  ** `timeoutSeconds` ** - wall-clock timeout for a single invocation. Default 3600.
+  ** `maxTokens` ** - token budget per invocation. Default N/A.
+  ** `idleRuntimeSessionTimeout` ** - how long an idle microVM stays warm. Default 900.
+  ** `maxLifetime` ** - maximum lifetime of a microVM session. Default 28800.

All limits are optional; omit them to use service defaults. Because harness is backed by AgentCore Runtime, harness invocations are also subject to Runtime service quotas. For more information, see [AgentCore harness Service Quotas](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/bedrock-agentcore-limits.html#harness-service-limits) and [AgentCore Runtime Service Quotas](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/bedrock-agentcore-limits.html#runtime-service-limits).

**Example**  

```
aws bedrock-agentcore-control update-harness \
  --harness-id "MyHarness-UuFdkQoXSL" \
  --max-iterations 50 \
  --timeout-seconds 1800 \
  --max-tokens 8192
```
Or override on a single invocation by passing `maxIterations`, `timeoutSeconds`, or `maxTokens` in `invoke_harness`.
Set defaults:  

```
agentcore add harness --name bounded-agent \
  --max-iterations 50 --timeout 1800 --max-tokens 8192 \
  --truncation-strategy sliding_window \
  --idle-timeout 600 --max-lifetime 14400
agentcore deploy
```
The `--truncation-strategy` flag accepts `sliding_window` or `summarization`. The `--idle-timeout` and `--max-lifetime` flags set lifecycle limits in seconds.  
Override on a single call:  

```
agentcore invoke --harness bounded-agent --max-iterations 20 --harness-timeout 600 \
  "Quick lookup: what's the weather in Seattle?"
```

## Tags
<a name="harness-tags"></a>

Apply tags to your harness for cost allocation and access control.

**Example**  

```
aws bedrock-agentcore-control create-harness \
  --harness-name "MyHarness" \
  --execution-role-arn "arn:aws:iam::123456789012:role/MyHarnessRole" \
  --tags '{"team": "platform", "environment": "staging"}'
```
Set tags in `harness.json`:  

```
{
  "tags": {
    "team": "platform",
    "environment": "staging"
  }
}
```
Run `agentcore deploy` to apply.

Tags flow through to deployed CloudFormation resources.

### Related topics
<a name="_related_topics"></a>
+  [Memory](harness-memory.md) - memory persists conversation context across sessions
+  [Environment and filesystem](harness-environment.md) - environment variables and custom containers
+  [Security and access controls](harness-security.md) - execution role policy and IAM permissions
+  [API Documentation](harness-get-started.md#api-documentation) 