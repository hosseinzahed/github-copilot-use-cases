# Azure AI Landing Zone Summary

## Overview
This document summarizes the Microsoft Azure AI Landing Zone guidance, which provides organizational processes and recommendations for building AI workloads in Azure at scale. The guidance focuses on AI-specific resource organization, connectivity, and integration with Azure Landing Zones.

## Key Concept
**Azure AI workloads do NOT require a separate AI landing zone.** Instead, AI workloads are deployed into existing Azure landing zone application subscriptions, just like any other application or service. The existing Azure landing zone architecture (with its design principles for identity, networking, security, and governance) is sufficient to support AI workloads.

## Core Components

### 1. Governance Boundaries for AI Workloads

**Management Group Separation:**
- Create separate management groups for internet-facing ("online") and internal ("corporate") AI workloads
- Establishes critical data governance boundaries to protect sensitive internal data
- Prevents external users from accessing internal business data
- Aligns with Azure landing zone management group architecture principles

**Policy Management:**
- Start with baseline Azure landing zone policies
- Add AI-specific Azure Policy definitions for:
  - Azure AI Foundry
  - Azure AI services
  - Azure AI Search
  - Azure Virtual Machines
- Ensures uniform governance across the platform
- Reduces manual compliance oversight

**Resource Deployment:**
- Deploy AI resources within workload-specific subscriptions
- AI resources inherit governance policies from workload management groups (not platform subscriptions)
- Prevents development bottlenecks from platform team controls
- Enables workload teams to operate with appropriate autonomy

### 2. Secure Connectivity for AI Workloads

**DDoS Protection:**
- Activate Azure DDoS Protection for internet-facing AI workloads
- Protects against distributed denial of service attacks
- Maintains service availability during attacks
- Implements protection at the virtual network level

**Operational Access:**
- Use Azure Bastion with jumpbox for secure operational access
- Prevents direct internet exposure of management interfaces
- Creates secure gateway for administrative tasks
- Maintains network isolation for AI resources

**On-Premises Connectivity Options:**

*Azure ExpressRoute (High-Volume Data Transfer):*
- Best for high data volumes and real-time processing
- Provides dedicated connectivity
- Includes FastPath feature for improved data path performance
- Delivers consistent performance

*Azure VPN Gateway (Moderate Data Transfer):*
- Suitable for moderate data volumes and infrequent data transfer
- Simpler setup and more cost-effective for smaller datasets
- Supports site-to-site VPN for cross-premises connectivity
- Supports point-to-site VPN for secure device access

### 3. AI Reliability Across Regions

**Multi-Region Deployment:**
- Deploy AI endpoints across at least two regions for production workloads
- Provides redundancy and high availability
- Enables faster failover during regional failures
- For Azure OpenAI: Use global deployments for automatic routing, or Azure API Management for load balancing regional deployments

**Regional Planning:**
- Verify AI service availability in target regions before deployment
- Different regions offer varying levels of service availability and features
- Check Azure service availability by region for required AI services
- Azure OpenAI offers multiple deployment models: global standard, global provisioned, regional standard, and regional provisioned

**Capacity Management:**
- Evaluate regional quota limits and capacity requirements
- Azure AI services have regional subscription limits
- Contact Azure support proactively for capacity needs exceeding standard quotas
- Prevents service disruptions during scaling

**Data Optimization:**
- Co-locate data with AI models in the same region for RAG (Retrieval-Augmented Generation) applications
- Reduces latency and improves data retrieval efficiency
- Cross-region configurations remain viable for specific business requirements

**Business Continuity:**
- Replicate critical AI assets to secondary regions:
  - Fine-tuned models
  - RAG datasets
  - Trained models
  - Training data
- Enables faster recovery during outages
- Maintains service availability across failure scenarios

### 4. AI Foundation Options

**Option A: Use Azure Landing Zone (Recommended)**
- Azure landing zone is the recommended starting point
- Provides predefined setup for platform and application resources
- Deploy AI workloads to dedicated application landing zones
- AI workloads integrate seamlessly within existing Azure landing zone architecture

**Option B: Build Custom AI Environment**
- If not using Azure landing zones, follow these recommendations:
- Create baseline resource hierarchy
- Segment internal AI workloads from internet-facing AI workloads
- Use policy to deny online access from customers for internal workloads
- Safeguards internal data from exposure to external users
- Use jumpbox for AI development and resource management

## Architectural Patterns

### AI Workload in Azure Landing Zone
AI workloads are deployed into application landing zones and leverage:
- Centralized platform landing zone resources for shared services
- Governance policies from management groups
- Cost efficiency through resource sharing
- Centralized identity, networking, and monitoring

### Baseline Resource Hierarchy
For organizations not using Azure landing zones:
- Separate management groups for different AI workload types
- Policy-driven access controls
- Jumpbox-based operational access
- Clear boundaries between internal and external-facing workloads

## Integration with Azure Services

### Azure AI Foundry
- Baseline chat architecture available as reference
- Integrates with Azure landing zones
- Provides guidance for infrastructure and agent deployment
- Supports grounding via enterprise data sources

### Azure API Management
- Acts as generative AI gateway
- Gateway offloading design pattern for AI models
- Manages traffic to AI endpoints with custom policies
- Enables governance of generative AI resources

### CycleCloud Workspace for Slurm
- Implementation option for AI on Azure infrastructure (IaaS)
- For organizations running AI workloads with Slurm scheduler
- Provides easy cluster creation and flexible management
- Offers full control of infrastructure

## Best Practices Summary

1. **Start with Azure landing zones** - Don't create separate AI landing zones
2. **Segment workloads by exposure** - Separate internet-facing from internal workloads
3. **Apply policy-based governance** - Use Azure Policy for consistent AI governance
4. **Secure connectivity** - Implement DDoS protection, Bastion, and appropriate on-premises links
5. **Plan for multi-region** - Deploy across regions for production workloads
6. **Verify regional capabilities** - Check service availability and quota limits before deployment
7. **Optimize data placement** - Co-locate data with models for performance
8. **Implement business continuity** - Replicate critical assets to secondary regions

## Additional Resources

- **Main Documentation**: [AI Ready - Cloud Adoption Framework](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/ai/ready)
- **Landing Zone Overview**: [What is an Azure landing zone?](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/)
- **Azure AI Foundry Landing Zone**: [Baseline architecture](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/baseline-azure-ai-foundry-landing-zone)
- **AI Adoption Scenario**: [Cloud Adoption Framework AI scenario](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/ai/)

---

*Document generated from Microsoft Learn documentation on November 6, 2025*
