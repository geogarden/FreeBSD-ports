# Created by: Rusmir Dusko <nemysis@FreeBSD.org>
# $FreeBSD$

PORTNAME=	send2trash
DISTVERSION=	1.5.0
CATEGORIES=	deskutils
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}
DISTNAME=	Send2Trash-${PORTVERSION}
DIST_SUBDIR=	python

MAINTAINER=	ports@FreeBSD.org
COMMENT=	Small package that sends files to the Trash

LICENSE=	BSD3CLAUSE

USES=		python:3.6+
USE_PYTHON=	distutils concurrent autoplist
NO_ARCH=	yes

PORTDOCS=	CHANGES.rst README.rst
OPTIONS_DEFINE=	DOCS

post-install-DOCS-on:
	@${MKDIR} ${STAGEDIR}${DOCSDIR}
	${INSTALL_DATA} ${PORTDOCS:S|^|${WRKSRC}/|} ${STAGEDIR}${DOCSDIR}

.include <bsd.port.mk>
