# Created by: Veniamin Gvozdikov <vg@FreeBSD.org>
# $FreeBSD$

PORTNAME=	server
PORTVERSION=	${GLPI_VER}.${FUNV_VER}
PORTREVISION=	1
PORTEPOCH=	1
CATEGORIES=	net-mgmt
PKGNAMEPREFIX=	glpi-plugins-fusioninventory-

MAINTAINER=	ports@FreeBSD.org
COMMENT=	Plugin of glpi to get information of networking devices

LICENSE=	AGPLv3

RUN_DEPENDS=	glpi>=0.90:www/glpi

USES=		gettext php shebangfix
USE_GITHUB=	yes
GH_ACCOUNT=	fusioninventory
GH_PROJECT=	fusioninventory-for-glpi
GH_TAGNAME=	glpi090+${FUNV_VER}
USE_PHP=	fileinfo simplexml

GLPI_VER=	0.90
FUNV_VER=	1.3
NO_BUILD=	yes
NO_ARCH=	yes

SHEBANG_FILES=	lib/mustache.js-2.0.0/hooks/install-hooks.sh \
		scripts/get_agent_jobs.php scripts/cleanup_repository.php \
		scripts/prepare_jobs.php scripts/get_job_logs.php \
		tools/extract_template.sh
PLIST_SUB=	WWWOWN=${WWWOWN} WWWGRP=${WWWGRP}

GLPIPLUGINDIR?=	www/glpi/plugins

.include <bsd.port.pre.mk>
do-install:
	@${MKDIR} -m 0755 ${STAGEDIR}${PREFIX}/${GLPIPLUGINDIR}
	@${CP} -R ${WRKSRC} ${STAGEDIR}${PREFIX}/${GLPIPLUGINDIR}/fusioninventory

.include <bsd.port.post.mk>
