"""
Mock Linear Issues for Jenkins CI/CD Testing

This module provides comprehensive mock Linear issues based on the Jenkins PRD
for testing the GitHub agent and Linear integration functionality.
"""

from datetime import datetime, timedelta
from typing import List, Dict, Any
from dataclasses import dataclass
import json


@dataclass
class MockLinearIssue:
    """Mock Linear issue structure for testing"""
    id: str
    title: str
    description: str
    state: str
    project_id: str
    assignee_id: str
    parent_id: str = None
    created_at: datetime = None
    updated_at: datetime = None
    milestone: str = None
    due_date: datetime = None
    priority: str = "Medium"
    labels: List[str] = None
    
    def __post_init__(self):
        if self.labels is None:
            self.labels = []
        if self.created_at is None:
            self.created_at = datetime.now() - timedelta(days=30)
        if self.updated_at is None:
            self.updated_at = datetime.now() - timedelta(days=1)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for API responses"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "state": self.state,
            "project_id": self.project_id,
            "assignee_id": self.assignee_id,
            "parent_id": self.parent_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "milestone": self.milestone,
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "priority": self.priority,
            "labels": self.labels
        }


def get_jenkins_mock_issues() -> List[MockLinearIssue]:
    """
    Generate comprehensive mock Linear issues for Jenkins CI/CD testing
    
    Issues are categorized based on Jenkins PRD features:
    1. Pipeline Automation
    2. Build & Test Management
    3. Version Control Integration
    4. Distributed Build System
    5. Plugin Ecosystem
    6. Security & Access Control
    7. Notifications & Reporting
    8. API & Automation
    """
    
    base_date = datetime.now() - timedelta(days=45)
    
    issues = [
        # ========== PIPELINE AUTOMATION ==========
        MockLinearIssue(
            id="JEN-001",
            title="Implement declarative pipeline syntax parser",
            description="Create parser for Jenkinsfile declarative syntax to enable pipeline-as-code functionality. Should support stages, steps, and conditional logic.",
            state="In Progress",
            project_id="jenkins-core",
            assignee_id="dev-001",
            created_at=base_date + timedelta(days=1),
            updated_at=datetime.now() - timedelta(days=2),
            milestone="Pipeline Core v2.0",
            priority="High",
            labels=["pipeline", "declarative", "parser", "jenkinsfile"]
        ),
        
        MockLinearIssue(
            id="JEN-002",
            title="Add Groovy scripted pipeline support",
            description="Implement scripted pipeline execution engine with Groovy DSL support for advanced pipeline customization.",
            state="To Do",
            project_id="jenkins-core",
            assignee_id="dev-002",
            parent_id="JEN-001",
            created_at=base_date + timedelta(days=2),
            milestone="Pipeline Core v2.0",
            priority="High",
            labels=["pipeline", "groovy", "scripted", "dsl"]
        ),
        
        MockLinearIssue(
            id="JEN-003",
            title="Multi-branch pipeline auto-discovery",
            description="Automatically detect and create pipelines for new branches in connected repositories. Should scan for Jenkinsfile presence.",
            state="Completed",
            project_id="jenkins-core",
            assignee_id="dev-003",
            created_at=base_date + timedelta(days=3),
            updated_at=base_date + timedelta(days=25),
            milestone="Pipeline Core v2.0",
            priority="Medium",
            labels=["pipeline", "multi-branch", "auto-discovery", "git"]
        ),
        
        MockLinearIssue(
            id="JEN-004",
            title="Pipeline visualization dashboard",
            description="Create visual pipeline execution dashboard showing stage progress, timing, and dependencies in real-time.",
            state="In Progress",
            project_id="jenkins-ui",
            assignee_id="dev-004",
            created_at=base_date + timedelta(days=4),
            updated_at=datetime.now() - timedelta(days=1),
            milestone="UI Enhancement v1.5",
            priority="Medium",
            labels=["pipeline", "visualization", "dashboard", "ui"]
        ),
        
        MockLinearIssue(
            id="JEN-005",
            title="Parallel stage execution engine",
            description="Implement parallel execution support for pipeline stages to improve build performance and resource utilization.",
            state="To Do",
            project_id="jenkins-core",
            assignee_id="dev-001",
            created_at=base_date + timedelta(days=5),
            milestone="Performance v1.0",
            priority="Medium",
            labels=["pipeline", "parallel", "performance", "execution"]
        ),
        
        # ========== BUILD & TEST MANAGEMENT ==========
        MockLinearIssue(
            id="JEN-006",
            title="Maven build tool integration",
            description="Enhanced Maven integration with dependency caching, multi-module support, and build optimization features.",
            state="Completed",
            project_id="jenkins-build-tools",
            assignee_id="dev-005",
            created_at=base_date + timedelta(days=6),
            updated_at=base_date + timedelta(days=30),
            milestone="Build Tools v2.1",
            priority="High",
            labels=["build", "maven", "java", "dependency"]
        ),
        
        MockLinearIssue(
            id="JEN-007",
            title="Gradle build optimization",
            description="Implement Gradle build caching and parallel execution to reduce build times for large projects.",
            state="In Progress",
            project_id="jenkins-build-tools",
            assignee_id="dev-006",
            created_at=base_date + timedelta(days=7),
            updated_at=datetime.now() - timedelta(days=3),
            milestone="Build Tools v2.1",
            priority="High",
            labels=["build", "gradle", "optimization", "caching"]
        ),
        
        MockLinearIssue(
            id="JEN-008",
            title="JUnit test report aggregation",
            description="Aggregate JUnit test results across multiple modules and provide comprehensive test reporting with trends.",
            state="To Do",
            project_id="jenkins-testing",
            assignee_id="dev-007",
            created_at=base_date + timedelta(days=8),
            milestone="Testing v1.3",
            priority="Medium",
            labels=["testing", "junit", "reporting", "aggregation"]
        ),
        
        MockLinearIssue(
            id="JEN-009",
            title="TestNG integration and reporting",
            description="Full TestNG test framework integration with parallel test execution and detailed result reporting.",
            state="To Do",
            project_id="jenkins-testing",
            assignee_id="dev-007",
            parent_id="JEN-008",
            created_at=base_date + timedelta(days=9),
            milestone="Testing v1.3",
            priority="Low",
            labels=["testing", "testng", "integration", "parallel"]
        ),
        
        MockLinearIssue(
            id="JEN-010",
            title="Build artifact management system",
            description="Implement artifact storage, versioning, and cleanup policies with integration to artifact repositories.",
            state="In Progress",
            project_id="jenkins-artifacts",
            assignee_id="dev-008",
            created_at=base_date + timedelta(days=10),
            updated_at=datetime.now() - timedelta(hours=12),
            milestone="Artifact Management v1.0",
            priority="High",
            labels=["artifact", "storage", "versioning", "cleanup"]
        ),
        
        # ========== VERSION CONTROL INTEGRATION ==========
        MockLinearIssue(
            id="JEN-011",
            title="GitHub webhook integration",
            description="Implement secure GitHub webhook handling for automatic build triggering on push, PR, and tag events.",
            state="Completed",
            project_id="jenkins-scm",
            assignee_id="dev-009",
            created_at=base_date + timedelta(days=11),
            updated_at=base_date + timedelta(days=35),
            milestone="SCM Integration v2.0",
            priority="High",
            labels=["github", "webhook", "integration", "trigger"]
        ),
        
        MockLinearIssue(
            id="JEN-012",
            title="GitLab CI/CD integration",
            description="Native GitLab integration supporting GitLab CI/CD pipelines, merge requests, and repository mirroring.",
            state="In Progress",
            project_id="jenkins-scm",
            assignee_id="dev-010",
            created_at=base_date + timedelta(days=12),
            updated_at=datetime.now() - timedelta(days=1),
            milestone="SCM Integration v2.0",
            priority="Medium",
            labels=["gitlab", "integration", "merge-request", "cicd"]
        ),
        
        MockLinearIssue(
            id="JEN-013",
            title="Bitbucket Server integration",
            description="Enterprise Bitbucket Server integration with support for pull request building and branch permissions.",
            state="To Do",
            project_id="jenkins-scm",
            assignee_id="dev-009",
            created_at=base_date + timedelta(days=13),
            milestone="SCM Integration v2.1",
            priority="Low",
            labels=["bitbucket", "enterprise", "pull-request", "permissions"]
        ),
        
        MockLinearIssue(
            id="JEN-014",
            title="SVN polling optimization",
            description="Optimize SVN repository polling for large repositories with incremental change detection.",
            state="To Do",
            project_id="jenkins-scm",
            assignee_id="dev-011",
            created_at=base_date + timedelta(days=14),
            milestone="SCM Integration v2.1",
            priority="Low",
            labels=["svn", "polling", "optimization", "incremental"]
        ),
        
        MockLinearIssue(
            id="JEN-015",
            title="Git LFS support implementation",
            description="Add Git Large File Storage (LFS) support for repositories with large binary assets.",
            state="In Progress",
            project_id="jenkins-scm",
            assignee_id="dev-012",
            created_at=base_date + timedelta(days=15),
            updated_at=datetime.now() - timedelta(days=4),
            milestone="SCM Integration v2.0",
            priority="Medium",
            labels=["git", "lfs", "large-files", "binary"]
        ),
        
        # ========== DISTRIBUTED BUILD SYSTEM ==========
        MockLinearIssue(
            id="JEN-016",
            title="Master-agent communication security",
            description="Implement encrypted communication between Jenkins master and build agents with certificate-based authentication.",
            state="Completed",
            project_id="jenkins-distributed",
            assignee_id="dev-013",
            created_at=base_date + timedelta(days=16),
            updated_at=base_date + timedelta(days=40),
            milestone="Security v1.0",
            priority="High",
            labels=["security", "master-agent", "encryption", "certificate"]
        ),
        
        MockLinearIssue(
            id="JEN-017",
            title="Kubernetes agent provisioning",
            description="Dynamic Kubernetes pod provisioning for build agents with auto-scaling and resource management.",
            state="In Progress",
            project_id="jenkins-k8s",
            assignee_id="dev-014",
            created_at=base_date + timedelta(days=17),
            updated_at=datetime.now() - timedelta(hours=6),
            milestone="Cloud Native v1.0",
            priority="High",
            labels=["kubernetes", "provisioning", "auto-scaling", "pods"]
        ),
        
        MockLinearIssue(
            id="JEN-018",
            title="Docker container build agents",
            description="Containerized build agents with custom Docker images and volume mounting for build artifacts.",
            state="In Progress",
            project_id="jenkins-docker",
            assignee_id="dev-015",
            created_at=base_date + timedelta(days=18),
            updated_at=datetime.now() - timedelta(days=2),
            milestone="Cloud Native v1.0",
            priority="High",
            labels=["docker", "container", "build-agent", "volume"]
        ),
        
        MockLinearIssue(
            id="JEN-019",
            title="AWS EC2 agent auto-scaling",
            description="AWS EC2 instance auto-scaling for build agents based on build queue depth and demand.",
            state="To Do",
            project_id="jenkins-cloud",
            assignee_id="dev-016",
            created_at=base_date + timedelta(days=19),
            milestone="Cloud Integration v1.0",
            priority="Medium",
            labels=["aws", "ec2", "auto-scaling", "cloud"]
        ),
        
        MockLinearIssue(
            id="JEN-020",
            title="Build queue management optimization",
            description="Intelligent build queue management with priority scheduling and resource allocation optimization.",
            state="To Do",
            project_id="jenkins-distributed",
            assignee_id="dev-013",
            created_at=base_date + timedelta(days=20),
            milestone="Performance v1.0",
            priority="Medium",
            labels=["queue", "scheduling", "priority", "optimization"]
        ),
        
        # ========== PLUGIN ECOSYSTEM ==========
        MockLinearIssue(
            id="JEN-021",
            title="Plugin marketplace UI redesign",
            description="Modern plugin marketplace interface with search, filtering, ratings, and installation tracking.",
            state="In Progress",
            project_id="jenkins-plugins",
            assignee_id="dev-017",
            created_at=base_date + timedelta(days=21),
            updated_at=datetime.now() - timedelta(days=1),
            milestone="Plugin System v3.0",
            priority="Medium",
            labels=["plugin", "marketplace", "ui", "search"]
        ),
        
        MockLinearIssue(
            id="JEN-022",
            title="Plugin dependency resolver",
            description="Automatic plugin dependency resolution and conflict detection with upgrade recommendations.",
            state="Completed",
            project_id="jenkins-plugins",
            assignee_id="dev-018",
            created_at=base_date + timedelta(days=22),
            updated_at=base_date + timedelta(days=38),
            milestone="Plugin System v3.0",
            priority="High",
            labels=["plugin", "dependency", "resolver", "conflict"]
        ),
        
        MockLinearIssue(
            id="JEN-023",
            title="Plugin security scanning",
            description="Automated security vulnerability scanning for plugins with risk assessment and recommendations.",
            state="To Do",
            project_id="jenkins-security",
            assignee_id="dev-019",
            created_at=base_date + timedelta(days=23),
            milestone="Security v1.1",
            priority="High",
            labels=["plugin", "security", "scanning", "vulnerability"]
        ),
        
        MockLinearIssue(
            id="JEN-024",
            title="Custom plugin development framework",
            description="Enhanced plugin development SDK with templates, testing framework, and documentation generation.",
            state="To Do",
            project_id="jenkins-sdk",
            assignee_id="dev-020",
            created_at=base_date + timedelta(days=24),
            milestone="Developer Experience v1.0",
            priority="Low",
            labels=["plugin", "sdk", "framework", "templates"]
        ),
        
        # ========== SECURITY & ACCESS CONTROL ==========
        MockLinearIssue(
            id="JEN-025",
            title="LDAP authentication integration",
            description="Enterprise LDAP/Active Directory authentication with group-based role mapping and SSO support.",
            state="Completed",
            project_id="jenkins-auth",
            assignee_id="dev-021",
            created_at=base_date + timedelta(days=25),
            updated_at=base_date + timedelta(days=42),
            milestone="Authentication v2.0",
            priority="High",
            labels=["ldap", "authentication", "active-directory", "sso"]
        ),
        
        MockLinearIssue(
            id="JEN-026",
            title="OAuth 2.0 provider integration",
            description="OAuth 2.0 authentication with support for GitHub, Google, and custom OAuth providers.",
            state="In Progress",
            project_id="jenkins-auth",
            assignee_id="dev-022",
            created_at=base_date + timedelta(days=26),
            updated_at=datetime.now() - timedelta(days=3),
            milestone="Authentication v2.0",
            priority="Medium",
            labels=["oauth", "authentication", "github", "google"]
        ),
        
        MockLinearIssue(
            id="JEN-027",
            title="Role-based access control (RBAC)",
            description="Granular RBAC system with job-level permissions, role inheritance, and permission templates.",
            state="In Progress",
            project_id="jenkins-security",
            assignee_id="dev-023",
            created_at=base_date + timedelta(days=27),
            updated_at=datetime.now() - timedelta(hours=8),
            milestone="Security v1.0",
            priority="High",
            labels=["rbac", "permissions", "roles", "access-control"]
        ),
        
        MockLinearIssue(
            id="JEN-028",
            title="Encrypted credentials management",
            description="Secure credential storage with encryption at rest, rotation policies, and audit logging.",
            state="Completed",
            project_id="jenkins-security",
            assignee_id="dev-024",
            created_at=base_date + timedelta(days=28),
            updated_at=base_date + timedelta(days=41),
            milestone="Security v1.0",
            priority="High",
            labels=["credentials", "encryption", "storage", "audit"]
        ),
        
        MockLinearIssue(
            id="JEN-029",
            title="Security audit logging",
            description="Comprehensive security audit logging with compliance reporting and anomaly detection.",
            state="To Do",
            project_id="jenkins-security",
            assignee_id="dev-025",
            created_at=base_date + timedelta(days=29),
            milestone="Security v1.1",
            priority="Medium",
            labels=["audit", "logging", "compliance", "security"]
        ),
        
        # ========== NOTIFICATIONS & REPORTING ==========
        MockLinearIssue(
            id="JEN-030",
            title="Slack notification integration",
            description="Rich Slack notifications with build status, test results, and interactive buttons for actions.",
            state="Completed",
            project_id="jenkins-notifications",
            assignee_id="dev-026",
            created_at=base_date + timedelta(days=30),
            updated_at=base_date + timedelta(days=43),
            milestone="Notifications v1.5",
            priority="Medium",
            labels=["slack", "notification", "integration", "interactive"]
        ),
        
        MockLinearIssue(
            id="JEN-031",
            title="Microsoft Teams integration",
            description="Microsoft Teams webhook integration with adaptive cards and build status notifications.",
            state="In Progress",
            project_id="jenkins-notifications",
            assignee_id="dev-027",
            created_at=base_date + timedelta(days=31),
            updated_at=datetime.now() - timedelta(days=2),
            milestone="Notifications v1.5",
            priority="Low",
            labels=["teams", "microsoft", "notification", "adaptive-cards"]
        ),
        
        MockLinearIssue(
            id="JEN-032",
            title="Build metrics dashboard",
            description="Real-time build metrics dashboard with performance trends, success rates, and bottleneck analysis.",
            state="To Do",
            project_id="jenkins-metrics",
            assignee_id="dev-028",
            created_at=base_date + timedelta(days=32),
            milestone="Analytics v1.0",
            priority="Medium",
            labels=["metrics", "dashboard", "analytics", "performance"]
        ),
        
        MockLinearIssue(
            id="JEN-033",
            title="Email notification templates",
            description="Customizable email notification templates with HTML formatting and embedded build information.",
            state="Completed",
            project_id="jenkins-notifications",
            assignee_id="dev-029",
            created_at=base_date + timedelta(days=33),
            updated_at=base_date + timedelta(days=44),
            milestone="Notifications v1.5",
            priority="Low",
            labels=["email", "notification", "templates", "html"]
        ),
        
        # ========== API & AUTOMATION ==========
        MockLinearIssue(
            id="JEN-034",
            title="REST API v2 implementation",
            description="Modern REST API with OpenAPI specification, rate limiting, and comprehensive endpoint coverage.",
            state="In Progress",
            project_id="jenkins-api",
            assignee_id="dev-030",
            created_at=base_date + timedelta(days=34),
            updated_at=datetime.now() - timedelta(hours=4),
            milestone="API v2.0",
            priority="High",
            labels=["rest-api", "openapi", "rate-limiting", "documentation"]
        ),
        
        MockLinearIssue(
            id="JEN-035",
            title="Jenkins CLI modernization",
            description="Updated Jenkins CLI with improved authentication, JSON output, and batch operations support.",
            state="To Do",
            project_id="jenkins-cli",
            assignee_id="dev-031",
            created_at=base_date + timedelta(days=35),
            milestone="CLI v2.0",
            priority="Medium",
            labels=["cli", "authentication", "json", "batch"]
        ),
        
        MockLinearIssue(
            id="JEN-036",
            title="Configuration as Code (JCasC)",
            description="YAML-based Jenkins configuration management with version control and automated deployment.",
            state="In Progress",
            project_id="jenkins-config",
            assignee_id="dev-032",
            created_at=base_date + timedelta(days=36),
            updated_at=datetime.now() - timedelta(days=1),
            milestone="Configuration v1.0",
            priority="High",
            labels=["jcasc", "yaml", "configuration", "automation"]
        ),
        
        MockLinearIssue(
            id="JEN-037",
            title="Webhook security and validation",
            description="Enhanced webhook security with signature validation, IP whitelisting, and rate limiting.",
            state="To Do",
            project_id="jenkins-webhooks",
            assignee_id="dev-033",
            created_at=base_date + timedelta(days=37),
            milestone="Security v1.1",
            priority="High",
            labels=["webhook", "security", "validation", "rate-limiting"]
        ),
        
        MockLinearIssue(
            id="JEN-038",
            title="Third-party tool integration framework",
            description="Standardized framework for integrating external tools with Jenkins pipelines and workflows.",
            state="To Do",
            project_id="jenkins-integrations",
            assignee_id="dev-034",
            created_at=base_date + timedelta(days=38),
            milestone="Integration v1.0",
            priority="Low",
            labels=["integration", "framework", "third-party", "tools"]
        ),
        
        # ========== PERFORMANCE & INFRASTRUCTURE ==========
        MockLinearIssue(
            id="JEN-039",
            title="Database query optimization",
            description="Optimize database queries for build history, user management, and configuration storage.",
            state="In Progress",
            project_id="jenkins-performance",
            assignee_id="dev-035",
            created_at=base_date + timedelta(days=39),
            updated_at=datetime.now() - timedelta(days=5),
            milestone="Performance v1.0",
            priority="Medium",
            labels=["database", "optimization", "query", "performance"]
        ),
        
        MockLinearIssue(
            id="JEN-040",
            title="Memory usage optimization",
            description="Reduce Jenkins master memory footprint through caching improvements and object lifecycle management.",
            state="To Do",
            project_id="jenkins-performance",
            assignee_id="dev-036",
            created_at=base_date + timedelta(days=40),
            milestone="Performance v1.0",
            priority="High",
            labels=["memory", "optimization", "caching", "lifecycle"]
        )
    ]
    
    return issues


def get_issues_by_category() -> Dict[str, List[MockLinearIssue]]:
    """Get issues organized by Jenkins PRD feature categories"""
    issues = get_jenkins_mock_issues()
    
    categories = {
        "Pipeline Automation": [],
        "Build & Test Management": [],
        "Version Control Integration": [],
        "Distributed Build System": [],
        "Plugin Ecosystem": [],
        "Security & Access Control": [],
        "Notifications & Reporting": [],
        "API & Automation": [],
        "Performance & Infrastructure": []
    }
    
    # Categorize based on labels and issue IDs
    for issue in issues:
        issue_id = int(issue.id.split('-')[1])
        
        if 1 <= issue_id <= 5:
            categories["Pipeline Automation"].append(issue)
        elif 6 <= issue_id <= 10:
            categories["Build & Test Management"].append(issue)
        elif 11 <= issue_id <= 15:
            categories["Version Control Integration"].append(issue)
        elif 16 <= issue_id <= 20:
            categories["Distributed Build System"].append(issue)
        elif 21 <= issue_id <= 24:
            categories["Plugin Ecosystem"].append(issue)
        elif 25 <= issue_id <= 29:
            categories["Security & Access Control"].append(issue)
        elif 30 <= issue_id <= 33:
            categories["Notifications & Reporting"].append(issue)
        elif 34 <= issue_id <= 38:
            categories["API & Automation"].append(issue)
        elif 39 <= issue_id <= 40:
            categories["Performance & Infrastructure"].append(issue)
    
    return categories


def get_issue_statistics() -> Dict[str, Any]:
    """Get statistics about the mock issues"""
    issues = get_jenkins_mock_issues()
    categories = get_issues_by_category()
    
    # State statistics
    state_counts = {}
    for issue in issues:
        state_counts[issue.state] = state_counts.get(issue.state, 0) + 1
    
    # Priority statistics
    priority_counts = {}
    for issue in issues:
        priority_counts[issue.priority] = priority_counts.get(issue.priority, 0) + 1
    
    # Category statistics
    category_counts = {cat: len(issues) for cat, issues in categories.items()}
    
    return {
        "total_issues": len(issues),
        "by_state": state_counts,
        "by_priority": priority_counts,
        "by_category": category_counts,
        "parent_issues": len([i for i in issues if i.parent_id is None]),
        "sub_issues": len([i for i in issues if i.parent_id is not None])
    }


def export_issues_json(filename: str = "jenkins_mock_issues.json") -> str:
    """Export mock issues to JSON file for testing"""
    issues = get_jenkins_mock_issues()
    issue_data = [issue.to_dict() for issue in issues]
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump({
            "issues": issue_data,
            "metadata": {
                "total_count": len(issues),
                "generated_at": datetime.now().isoformat(),
                "categories": list(get_issues_by_category().keys())
            }
        }, f, indent=2)
    
    return filename


# Usage examples and testing
if __name__ == "__main__":
    # Generate and display issue statistics
    stats = get_issue_statistics()
    print("Jenkins Mock Issues Statistics:")
    print("=" * 40)
    print(f"Total Issues: {stats['total_issues']}")
    print(f"Parent Issues: {stats['parent_issues']}")
    print(f"Sub Issues: {stats['sub_issues']}")
    
    print("\nBy State:")
    for state, count in stats['by_state'].items():
        print(f"  {state}: {count}")
    
    print("\nBy Priority:")
    for priority, count in stats['by_priority'].items():
        print(f"  {priority}: {count}")
    
    print("\nBy Category:")
    for category, count in stats['by_category'].items():
        print(f"  {category}: {count}")
    
    # Export to JSON for testing
    json_file = export_issues_json()
    print(f"\nIssues exported to: {json_file}")
    
    # Display a few sample issues
    print("\nSample Issues:")
    print("-" * 40)
    issues = get_jenkins_mock_issues()
    for issue in issues[:3]:
        print(f"[{issue.id}] {issue.title}")
        print(f"  State: {issue.state} | Priority: {issue.priority}")
        print(f"  Labels: {', '.join(issue.labels)}")
        print()
